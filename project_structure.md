
# Project Structure
```
Whatsapp_Chatbot_v3/
└── app/
│   ├── config.py
│   ├── controllers/
│   │   ├── chatbot_controller.py
│   │   ├── health_controller.py
│   │   └── tables_controller.py
│   ├── core/
│   │   └── robot/
│   │       ├── entryPoint.py
│   │       └── saveMessage.py
│   ├── interfaces/
│   │   ├── api/
│   │   │   └── whatsapp_api.py
│   │   ├── crud/
│   │   │   └── models_repo.py
│   │   └── generator/
│   │       └── msg/
│   │           └── json_format.py
│   ├── models/
│   │   ├── database/
│   │   │   └── db.py
│   │   └── orm/
│   │       └── databaseModels.py
│   ├── services/
│   │   └── modelServices.py
│   ├── stack/
│   │   └── constant/
│   │       ├── messages_list.py
│   │       ├── webdomain.py
│   │       └── whatsapp.py
│   └── web/
│       ├── static/
│       └── templates/
├── requirements.txt
└── run.py
```