// src/app/page.js

export default async function HomePage() {
  const res = await fetch('http://localhost:8000/api/schools/');
  const schools = await res.json();

  return (
      <div>
          <h1>Schools</h1>
          <ul>
              {schools.map((school) => (
                  <li key={school.id}>{school.name}</li>
              ))}
          </ul>
      </div>
  );
}
