import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'dart:io';
import 'package:mime/mime.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import 'package:http_parser/http_parser.dart';
import 'package:shared_preferences/shared_preferences.dart';

class UserProfileProvider with ChangeNotifier {
  String? _firstName;
  String? _lastName;
  String? _username;
  String? _accessToken;
  String? _profilePicture;

  String? get firstName => _firstName;
  String? get lastName => _lastName;
  String? get username => _username;
  String? get accessToken => _accessToken;
  String? get profilePicture => _profilePicture;

  Future<void> init() async {
    await fetchUserProfile();
    notifyListeners();
  }

  final String baseUrl = "http://127.0.0.1:8000/api/";

  // Fetch user profile
  Future<void> fetchUserProfile() async {
    SharedPreferences sharedPreferences = await SharedPreferences.getInstance();
    _accessToken = sharedPreferences.getString("access");
    final url = Uri.parse("${baseUrl}users/me/");

    try {
      final response = await http.get(
        url,
        headers: {
          'Authorization': 'Bearer $_accessToken',
        },
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        print(data.toString());
        _firstName = data['firstname'];
        _lastName = data['lastname'];
        _username = data['username'];
        _profilePicture = data['profile_picture'];
        notifyListeners();
      } else {
        throw Exception(
            'Failed to fetch profile. Status Code: ${response.statusCode}');
      }
    } catch (error) {
      rethrow;
    }
  }

  // Update user profile
  Future<void> updateUserProfile(
      String firstName, 
      String lastName, 
      String username,
      {XFile? imageFile}) async {
    final url = Uri.parse("${baseUrl}users/update_profile/");
    
    try {
      var request = http.MultipartRequest("PUT", url);
      request.headers['Authorization'] = 'Bearer $_accessToken';

      // Add user details as text fields
      request.fields['firstname'] = firstName;
      request.fields['lastname'] = lastName;
      request.fields['username'] = username;

      // If an image is provided, attach it as a file
      if (imageFile != null) {
        print("Uploading Image: ${imageFile.name}, Path: ${imageFile.path}");
        if (kIsWeb) {
          print("bangpusi");
          Uint8List? bytes = await imageFile.readAsBytes();
          String fileName = imageFile.name.isNotEmpty 
              ? imageFile.name 
              : "profile.jpg"; // Default name if missing
          String mimeType = lookupMimeType(imageFile.name) ?? 'image/jpeg';

          print("Detected MIME Type: $mimeType");
          print("Image Bytes Length: ${bytes.length}");

          request.files.add(http.MultipartFile.fromBytes(
            'profile_picture',
            bytes,
            filename: fileName, 
            
          ));
        } else {
          if (!File(imageFile.path).existsSync()) {
            throw Exception("File does not exist: ${imageFile.path}");
          }
          print("bangdik");

          request.files.add(await http.MultipartFile.fromPath(
            'profile_picture', 
            imageFile.path
          ));
        }
      }

      print("Request Fields: ${request.fields}");
      print("Headers: ${request.headers}");

      var response = await request.send();
      // var responseBody = await response.stream.bytesToString();
      // print("Response Body: $responseBody");

      if (response.statusCode == 200) {
        var responseData = await response.stream.bytesToString();
        final data = json.decode(responseData);
        print("Response Body: $responseData");

        _firstName = data['firstname'];
        _lastName = data['lastname'];
        _username = data['username'];
        _profilePicture = data['profile_picture']; // Update stored profile picture
        notifyListeners();
      } else {
        throw Exception('Failed to update profile. Status Code: ${response.statusCode}');
      }
    } catch (error) {
      rethrow;
    }
  }
}
