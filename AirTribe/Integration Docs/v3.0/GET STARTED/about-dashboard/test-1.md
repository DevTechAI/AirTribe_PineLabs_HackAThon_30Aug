---
title: "Test"
slug: "test-1"
excerpt: ""
hidden: true
createdAt: "Fri Feb 28 2025 10:11:10 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Feb 28 2025 10:12:13 GMT+0000 (Coordinated Universal Time)"
---
[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid blue;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div>\n        <div class=\"tab active\" onclick=\"\n            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));\n            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));\n            this.classList.add('active');\n            document.getElementById('tab1').classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" onclick=\"\n            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));\n            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));\n            this.classList.add('active');\n            document.getElementById('tab2').classList.add('active');\n        \">Response Parameters</div>\n    </div>\n\n    <div id=\"tab1\" class=\"tab-content active\">\n        <p>Content for Request Parameters.</p>\n    </div>\n    <div id=\"tab2\" class=\"tab-content\">\n        <p>Content for Response Parameters.</p>\n    </div>\n\n</body>\n</html>\n"
}
[/block]


[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid blue;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div>\n        <div class=\"tab active\" onclick=\"switchTab(event, 'tab1')\">Request Parameters</div>\n        <div class=\"tab\" onclick=\"switchTab(event, 'tab2')\">Response Parameters</div>\n    </div>\n\n    <div id=\"tab1\" class=\"tab-content active\">\n      <p>This is the Request Parameters content.</p>\n    <div id=\"tab2\" class=\"tab-content\">\n        <p>This is the Response Parameters content.</p>\n    </div>\n\n    <script>\n        function switchTab(event, tabId) {\n            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));\n            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));\n            \n            event.currentTarget.classList.add('active');\n            document.getElementById(tabId).classList.add('active');\n        }\n    </script>\n</body>\n</html>\n"
}
[/block]
