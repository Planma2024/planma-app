import 'package:flutter/material.dart';

class TaskItem extends StatefulWidget {
  final String taskName;
  final String subject;
  final String duration;
  final IconData icon;
  final String priority; // Added priority field

  TaskItem({
    required this.taskName,
    required this.subject,
    required this.duration,
    required this.icon,
    required this.priority, // Pass priority here
  });

  @override
  _TaskItemState createState() => _TaskItemState();
}

class _TaskItemState extends State<TaskItem> {
  bool isChecked = false;

  void toggleCheckbox() {
    setState(() {
      isChecked = !isChecked;
    });
  }

  Color getPriorityColor(String priority) {
    switch (priority) {
      case 'High':
        return Colors.red; // High priority - red
      case 'Medium':
        return Colors.orange; // Medium priority - orange
      case 'Low':
        return Colors.green; // Low priority - green
      default:
        return Colors.grey; // Default color for no priority
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(vertical: 5),
      padding: EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: Colors.blue[100],
        borderRadius: BorderRadius.circular(10),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              GestureDetector(
                onTap: toggleCheckbox,
                child: Container(
                  width: 24,
                  height: 24,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: isChecked ? Colors.green : Colors.white,
                    border: Border.all(
                        color: Colors.black26), // Border for visual clarity
                  ),
                  child: isChecked
                      ? Icon(
                          Icons.check,
                          size: 16,
                          color: Colors.white,
                        )
                      : null,
                ),
              ),
              SizedBox(width: 10),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    widget.taskName,
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  Text('${widget.subject} (${widget.duration})'),
                ],
              ),
            ],
          ),
          Row(
            children: [
              Icon(
                widget.icon, // Flag icon
                color: getPriorityColor(
                    widget.priority), // Set flag color based on priority
                size: 24, // Icon size
              ),
            ],
          ),
        ],
      ),
    );
  }
}
