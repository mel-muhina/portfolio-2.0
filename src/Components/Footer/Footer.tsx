import styles from './Footer.module.css';

const CONTACT = {
  name: 'Mel Muhina',
  tagline:
    'Full-Stack Software Engineer building responsive interfaces, robust APIs, and cloud-native systems.',
  email: 'mel.muhina@gmail.com',
  location: 'London, United Kingdom',
};

const SOCIALS = [
  { label: 'GitHub', prefix: 'gh/', handle: 'mel-muhina', href: 'https://github.com/mel-muhina' },
  { label: 'LinkedIn', prefix: 'in', handle: 'melmuhina', href: 'https://www.linkedin.com/in/melmuhina/' },
  { label: 'Email', prefix: '✉', handle: CONTACT.email, href: `mailto:${CONTACT.email}` },
];

const CORE_STACK = [
  'TypeScript',
  'React',
  'Node.js',
  'Python / FastAPI',
  'Java / Spring Boot',
  'AWS',
];

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className={styles['glass-footer']} id='contact'>
      <div className={`${styles['content-constraint']} ${styles['footer-content']}`}>
        <div className={styles['footer-columns-grid']}>
          <div>
            <div className={styles['brand-cluster']} style={{ marginBottom: '0.75rem' }}>
              <span className={styles['brand-name']} style={{ fontSize: '1.2rem' }}>
                {CONTACT.name}
              </span>
            </div>
            <p className={styles['footer-tagline']}>{CONTACT.tagline}</p>
            <div className={styles['footer-status']}>
              <span className={styles['green-radiant-pulse']}></span>
              <span
                style={{
                  fontFamily: 'var(--font-mono)',
                  fontSize: '0.75rem',
                  color: 'var(--color-text-dim)',
                }}
              >
                {CONTACT.location}
              </span>
            </div>
          </div>

          <div>
            <span className={styles['footer-col-label']}>Core Stack</span>
            <div className={styles['arsenal-badge-flow']} style={{ marginTop: '0.85rem' }}>
              {CORE_STACK.map((tech) => (
                <span key={tech} className={styles['frosted-badge']}>
                  {tech}
                </span>
              ))}
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
            <span className={styles['footer-col-label']}>Connect</span>
            <div className={styles['footer-social-list']}>
              {SOCIALS.map((social) => (
                <a
                  key={social.label}
                  className={styles['nav-pill']}
                  href={social.href}
                  target={social.href.startsWith('http') ? '_blank' : undefined}
                  rel={social.href.startsWith('http') ? 'noopener noreferrer' : undefined}
                  style={{
                    color: 'var(--color-text-muted)',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '0.35rem',
                  }}
                >
                  <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--color-primary)' }}>
                    {social.prefix}
                  </span>
                  {social.handle}
                </a>
              ))}
            </div>
          </div>
        </div>

        <div className={styles['footer-bottom-bar']}>
          <span>© {year} {CONTACT.name}. All rights reserved.</span>
        </div>
      </div>
    </footer>
  );
}
