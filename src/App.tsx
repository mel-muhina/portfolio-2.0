import './App.css';
import './globals.css';
import { Navbar, About, Hero, Experience, Footer } from './Components';
import Layout from './Components/Layout/Layout.tsx';
import Timeline from './Components/Timeline/Timeline.tsx';
import Skills from './Skills/Skills.tsx';
import Projects from './Components/Projects/Projects.tsx';

function App() {
  return (
    <div className="App">
      <Navbar />
      <main>
        <Hero />
        <div className="innerContainer">
          <Layout>
            <Skills />
            <Projects />
            <Timeline />
          </Layout>
        </div>
      </main>
    </div>
  );
}

export default App;
