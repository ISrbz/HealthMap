import bodyImage from "/assets/body-diagram.png";

export default function HeroSection() {
  const handleBodyClick = (part) => {
    alert(`You clicked on: ${part}`);
    // Later: redirect or fetch API symptoms for this part
  };

  return (
    <section className="text-center py-12">
      <h2 className="text-3xl font-bold mb-4">Understand Your Body Better</h2>
      <p className="mb-8">Click on any body part to learn about symptoms and treatments.</p>
      <div className="flex justify-center gap-8 p-4">
        <div className="bg-green-50 p-4 rounded shadow w-48">
          <h3 className="font-semibold mb-2">Common Issues</h3>
          <ul className="text-left list-disc list-inside">
            <li>Headaches</li>
            <li>Joint Pain</li>
            <li>Back Pain</li>
            <li>Muscle Strain</li>
          </ul>
        </div>
        <img src={bodyImage} alt="Body Diagram" className="w-48 cursor-pointer" onClick={() => handleBodyClick("Head")} />
        <div className="bg-green-50 p-4 rounded shadow w-48">
          <h3 className="font-semibold mb-2">Quick Actions</h3>
          <ul className="text-left space-y-2">
            <li>🔍 Search Symptoms</li>
            <li>👨‍⚕️ Find Doctors</li>
            <li>📄 Emergency Info</li>
            <li>📅 Book Appointment</li>
          </ul>
        </div>
      </div>
    </section>
  );
}
