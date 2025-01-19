# Discord-bot's Readme

## **Overview**  
The purpose of this wiki is to guide you through contributing to the development and improvement of HacklyBot, all while ensuring the security of sensitive data such as API tokens and bot activity.  

### **Why**  
The goal is to foster collaborative creation in a public space. Share your ideas, discuss your technical challenges, and avoid working in isolation—this is a group effort! Keep comments concise and not overly technical to encourage collaboration and creativity.  

### **What**  
We aim to build HacklyBot together. You’ll start with a shared base code available on GitHub, which everyone can access and modify. Share your progress, ideas, and challenges openly with the group. If you create something great, we’ll merge your contributions into the main bot’s code.  

### **How**  
We’ve created a dedicated test server where you can:  
- Create and test your own bot.  
- Collaborate with others and share feedback.  
- See and learn from the work of others.  
When you make changes, explain your ideas in the chat, share your updated code with the group, and work together to refine the bot.  

# **Tutorial: Add and Host Your Bot on the Test Server**

## **Step 1: Join the Test Server**  
Join our Discord test server by clicking this link: [https://discord.gg/CQTaBVRp](https://discord.gg/CQTaBVRp)  
Once you’re on the server, you can collaborate with other contributors and test your bot.

---
(You can also keep your bot in local and dont host it online)
## **Step 2: Create and Host Your Bot**

### **A) Create Your Bot on the Discord Developer Portal**  
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and click **"New Application."**  
2. Choose a name for your bot and click **"Create."**  
3. Navigate to the **"Bot"** tab, click **"Reset Token"**, and copy the new token. Save it somewhere safe—you’ll need it later.  
4. Go to the **OAuth2** tab, then under the **Scopes** section, check **"bot."**  
5. Scroll down to **Bot Permissions** and check the following permissions:  
   - View Channels  
   - Send Messages  
   - Send Messages in Threads  
   - Read Message History  
6. Copy the generated URL and send it to **@mugiballa** on Discord. He will review and add your bot to the test server.

---

### **B) Host Your Bot**

#### **1. Set Up Free Hosting**  
1. Go to [Pylexnodes](https://pylexnodes.net/) and click on **"Free Hosting"**, then select **"Discord"**, and authorize the app.  
2. On the Dashboard, click **"Create a New Server."**  
3. Choose a name for your server, scroll down to select **Python**, and then click **"Create."**  
4. Once created, click on the **"Panel Info"** tab. Copy the second line (password) and click **"Go to Panel."**  
5. Log in to the panel using your email and the password you copied.  

#### **2. Upload Your Bot Code**  
1. Click on your server name in the dashboard.  
2. Visit [this GitHub link](https://github.com/gethackly/Discord-bot/blob/main/Main.py) and copy the code provided there.  
3. In the hosting panel, go to the **Files** tab, click **"New File,"** and paste the copied code.  
4. Replace **"YOUR_TOKEN_HERE"** in the code with the bot token you copied earlier.  
5. Name the file **main.py** and click **"Create File."**  

#### **3. Configure Startup Settings**  
1. Go to the **Startup** tab in the hosting panel.  
2. Select the correct Python version for your bot (if you’re unsure, open a terminal on your computer and type `python --version`).  
3. In the **Additional Python Packages** field, type **discord**.  

#### **4. Start Your Bot**  
1. Navigate to the **Console** tab in the panel.  
2. Click **"Start"** to run your bot.  

---

## **Step 3: Congratulations!**  
Your bot should now be online and visible on the test server. You’re all set to start contributing! 🎉  

If you encounter any issues, feel free to ask for help on the test server.
