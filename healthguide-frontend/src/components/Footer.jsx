export default function Footer() {
    return (
      <footer className="bg-green-700 text-white p-6 mt-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div>
            <h5 className="font-bold mb-2">About HealthGuide</h5>
            <p>Your trusted source for understanding symptoms and care options.</p>
          </div>
          <div>
            <h5 className="font-bold mb-2">Quick Links</h5>
            <ul>
              <li>Symptom Checker</li>
              <li>Find a Doctor</li>
              <li>Medical Articles</li>
            </ul>
          </div>
          <div>
            <h5 className="font-bold mb-2">Contact</h5>
            <p>support@healthguide.com</p>
            <p>1-800-HEALTH</p>
          </div>
          <div>
            <h5 className="font-bold mb-2">Follow Us</h5>
            <p>📘 📷 🐦</p>
          </div>
        </div>
        <div className="text-center mt-4 text-sm">© 2025 HealthGuide. All rights reserved.</div>
      </footer>
    );
  }
  