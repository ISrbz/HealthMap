import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="flex justify-between items-center p-4 shadow">
      <h1 className="text-2xl font-bold text-green-600">HealthGuide</h1>
      <div className="space-x-6">
        <Link to="/" className="hover:text-green-600">Home</Link>
        <Link to="/symptoms" className="hover:text-green-600">Symptoms</Link>
        <a href="#" className="hover:text-green-600">Treatments</a>
        <a href="#" className="hover:text-green-600">About</a>
        <a href="#" className="hover:text-green-600">Contact</a>
      </div>
    </nav>
  );
}
