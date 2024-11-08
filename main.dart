import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('AI GUI with Python'),
        ),
        body: Center(
          child: ElevatedButton(
            onPressed: callPythonAPI,
            child: const Text('Run Python Code'),
          ),
        ),
      ),
    );
  }

  // Function to call the Python API
  Future<void> callPythonAPI() async {
    final response = await http.get(Uri.parse('http://127.0.0.1:5000/run_code'));
    
    if (response.statusCode == 200) {
      var data = jsonDecode(response.body);
      print(data["message"]);  // Output the message from the Python server
    } else {
      print("Failed to load data");
    }
  }
}
