# Flask Vercel Hello World

A minimal deployment smoke test for running a **Python Flask** application on **Vercel**. 

## 🛠️ Stack
* **Language:** Python
* **Framework:** Flask
* **Deployment Platform:** Vercel

---

## 🚀 Local Development

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbdulHadi117/flask-vercel-hello.git
   cd flask-vercel-hello
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   flask -app app run
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to view the application.

---

## 🌐 Deployment to Vercel

### Prerequisites
Make sure you have the [Vercel CLI](https://vercel.com/cli) installed:
```bash
npm i -g vercel
```

### Deploying
1. Log in to your Vercel account via CLI:
   ```bash
   vercel login
   ```
2. Deploy the project:
   ```bash
   vercel
   ```

### 🔗 Live Demo
* **Live URL:** [(https://flask-vercel-hello-sigma.vercel.app/)](https://flask-vercel-hello-sigma.vercel.app/)
