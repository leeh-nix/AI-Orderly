## AI-Orderly: Food Ordering with WhatsApp & AI

**AI-Orderly** is a Python application that allows users to order food through WhatsApp using natural language processing. It utilizes the power of AI to understand user text messages and streamline the ordering process.

**Features:**

* **WhatsApp Integration:** Seamless food ordering through familiar WhatsApp chat interface.
* **Natural Language Processing (NLP):** Utilizes the Gemini API to understand user intent and menu preferences.
* **Menu Browsing:** Users can browse menus directly within WhatsApp.
* **Order Customization:** Allows users to customize orders, including size, toppings, and special requests.
* **Database Storage:** Order data is stored securely in a PostgreSQL database with Prisma as the ORM (Object-Relational Mapper).
* **Backend Framework:** Built with Flask, a lightweight and flexible Python web framework.

**Getting Started**

### Prerequisites

* Python 3.x with `pip` installed
* PostgreSQL database server
* A WhatsApp Business API account
* A Gemini API account

### Installation

1. Clone this repository:

```bash
git clone https://github.com/leeh-nix/AI-Orderly.git
```

2. Navigate to the project directory:

```bash
cd AI-Orderly
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

* Copy the `.env.example` file to `.env`.
* Update the `.env` file with your specific details for:
    * WhatsApp API credentials
    * Gemini API key
    * PostgreSQL connection details

5. Set up the database:
    * Create a PostgreSQL database and user.
    * Update the connection details in `.env`.
    * Run the following command to create the database schema based on your models:
    ```bash
    prisma db push
    ```


**Usage**

To be updated!

**Notes:**

* This project requires further development to implement functionality like integrating with specific restaurant APIs or payment gateways.
* Refer to the documentation for detailed configuration instructions.
    * Flask (https://flask.palletsprojects.com/)
    * PostgreSQL (https://www.postgresql.org/docs/)
    * Prisma (https://www.prisma.io/docs/)
    * WhatsApp Business API (https://developers.facebook.com/docs/whatsapp/)
    * Gemini API (https://blog.google/technology/ai/google-gemini-ai/)

**Contributing**

We welcome contributions to this project! Please see the CONTRIBUTING.md file for guidelines on how to contribute.

**Disclaimer:**

This project is provided for educational purposes only. It is your responsibility to comply with the terms of service of any third-party APIs used.
