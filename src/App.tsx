import './App.css';
import './globals.css';
import { Navbar, Hero, Layout, Timeline, Skills, Projects } from './Components';

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
