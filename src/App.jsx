import './App.css';
import { Navbar, About, Hero, Experience, Footer, Projects } from "./Components";
// import { Hero } from "./components/Hero/Hero";
// import { Hero2 } from "./components/Hero2/Hero2";
// import { About } from "./components/About/About";
// import { Experience } from "./components/Experience/Experience";
// import { Projects } from "./components/Projects/Projects";
// import { Footer } from "./components/Footer/Footer";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Hero />
      <About />
      <Experience />
      <Projects />
      <Footer />
    </div>
  );
}

export default App;