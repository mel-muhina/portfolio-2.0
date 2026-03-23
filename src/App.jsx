import './App.css';
import { Navbar, About, Hero, Experience, Footer, Projects } from "./Components";

function App() {
  return (
    <div className="App">
        <div className="innerContainer">
          <Navbar />
          <Hero />
          <About />
          <Experience />
          <Projects />
          <Footer />
        </div>
    </div>
  );
}

export default App;