### 🧑‍💻 User Registration and KYC

This module allows users to register on the platform securely using a unique email and password. After registration, users are prompted to complete **KYC (Know Your Customer)** verification, which includes uploading identification documents (like Aadhaar or Passport), a profile picture, and other relevant details. This process ensures user authenticity and compliance with platform policies. The system validates uploaded files, checks data consistency, and updates the user’s KYC status to *Pending*, *Approved*, or *Rejected* based on admin verification.

### ⚙️ Account Creation

Once users complete KYC, they can proceed to **account creation**, where they can set up their personalized dashboard or profile based on the application requirements. This process leverages **Django** on the backend for managing models and data integrity, while **HTML, CSS, and JavaScript** are used to create interactive and responsive forms. Data interaction is handled using Django’s **ORM (Object-Relational Mapper)**, ensuring smooth database operations like user data storage, validation, and retrieval.

### 🛠️ Tech Stack

* **Backend:** Django (Python-based web framework)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite / PostgreSQL (via Django ORM)
* **Core Features:**

  * Secure user authentication and authorization
  * KYC document management and admin approval system
  * Error handling for missing or invalid inputs
  * Responsive frontend with interactive feedback

**Step-by-Step User Onboarding & KYC Flow**

This setup ensures a smooth, secure, and user-friendly flow from registration to KYC verification and final account activation.


After successfully registering on the platform, users are immediately redirected to the KYC upload page. Here, they must fill in their details and upload their required documents. Once submitted, this data is securely stored both in the Django admin interface and in the underlying MySQL database.

For users wishing to check their KYC verification status, the system provides a dedicated KYC status page. To access their status, users simply need to log in; the page then displays whether their KYC has been "approved," "rejected," or is still "pending." All registered user information, as well as KYC submissions, are systematically maintained in the database for easy access and management.

This workflow ensures a smooth and secure registration process, seamless KYC document submission, and transparent status tracking for every user.
