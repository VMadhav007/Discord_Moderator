🚨 Discord Toxicity Moderator Bot 🚨
====================================
A powerful Discord bot that uses ML to detect and moderate toxic language in your server, ensuring a safe and welcoming community.

🌟 Features
-----------
✅ Toxicity Detection: Leverages a pre-trained NLP model to identify toxic language in messages. 
✅ Automatic Moderation: Deletes toxic messages and warns users. 
✅ Timeouts: Automatically times out users after three consecutive toxic messages. 
✅ Real-Time Feedback: Provides immediate notifications and moderation actions. 
✅ Customizable: Adjust thresholds and timeout durations to suit your server's needs.

🚀 Getting Started
------------------
 1️⃣ Clone the Repository
    git clone https://github.com/VMadhav007/Discord_Moderator.git
    cd DiscordModerator
 2️⃣ Set Up Virtual Environment
    python -m venv venv  
    source venv/bin/activate   On Windows, use venv\Scripts\activate
 3️⃣ Install Dependencies
    pip install -r requirements.txt
 4️⃣ Configure Environment Variables
Create a .env file in the root directory and add your Discord bot token:
    DISCORD_ID=your-bot-token
    
 5️⃣ Run the Bot
    python main.py
    
🔗 Invite the Bot to Your Server
--------------------------------

[Click here to invite the bot to your server! 🎉](https://discord.com/oauth2/authorize?clientid=1386386567253458986)

🛠️ How It Works
----------------

1.  Monitor Messages: Listens to all messages sent in channels it has permission to access.
2.  Analyze Toxicity: Uses a pre-trained NLP model (e.g., XLM-RoBERTa) to evaluate messages for toxic content.
3.  Track Infractions: Keeps a count of each user's toxic messages.
4.  Timeout Rule: After 3 consecutive toxic messages, the user is automatically timed out.
5.  Moderation Feedback: Warns users about their behavior and notifies moderators of actions taken.

🖼️ Example
-----------

Here’s an example of how the bot interacts with users:
   Toxic Message Detected: User: "This is such a toxic comment!" Bot: "Hey @user, please avoid using toxic language!"
   After 3 Violations: Bot: "User @user has been timed out for repeated violations of server rules."
    
📚 Dependencies
---------------

   [discord.py](https://github.com/Rapptz/discord.py)
   [transformers](https://github.com/huggingface/transformers)
   Python 3.10+


🤝 Contributing
---------------
We welcome contributions to make this bot even better!

   Report bugs by opening an issue.
   Submit improvements via pull requests.

📄 License
----------
This project is licensed under the [MIT License](./LICENSE).


🌐 Connect with the Project
---------------------------
   [GitHub Repository](https://github.com/VMadhav007/DiscordModerator)
   [Invite the Bot](https://discord.com/oauth2/authorize?clientid=1386386567253458986)
