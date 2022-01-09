import 'package:flutter/material.dart';
import 'package:http/http.dart';

class CreatePage extends StatefulWidget {
  const CreatePage({
    Key? key,
    required this.client,
  }) : super(key: key);
  final Client client;

  @override
  _CreatePageState createState() => _CreatePageState();
}

class _CreatePageState extends State<CreatePage> {
  TextEditingController controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("追加する"),
      ),
      body: Column(children: [
        TextField(
          controller: controller,
          maxLines: 10,
        ),
        ElevatedButton(
          onPressed: () {
            widget.client.post(
              Uri.parse("http://127.0.0.1:8000/notes/create/"),
              body: {'body': controller.text},
            );
            Navigator.pop(context);
          },
          child: const Text("追加"),
        ),
      ]),
    );
  }
}
