import styles from './Footer.module.css';

const CONTACT = {
  name: 'Mel Muhina',
  tagline:
    'Full-Stack Software Engineer building responsive interfaces, robust APIs, and cloud-native systems.',
  email: 'mel.muhina@gmail.com',
  location: 'London, United Kingdom',
} as const;

const SOCIALS = [
  { label: 'GitHub', prefix: 'gh', handle: 'mel-muhina', href: 'https://github.com/mel-muhina' },
  { label: 'LinkedIn', prefix: 'in', handle: 'melmuhina', href: 'https://www.linkedin.com/in/melmuhina/' },
  { label: 'Email', prefix: '✉', handle: CONTACT.email, href: `mailto:${CONTACT.email}` },
] as const;

const CORE_STACK = [
  'TypeScript',
  'React',
  'Node.js',
  'Python / FastAPI',
  'Java / Spring Boot',
  'AWS',
] as const;

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className={styles.glassFooter} id="contact">
      <div className={`${styles.contentConstraint} ${styles.footerContent}`}>
        <div className={styles.footerColumnsGrid}>
          <div>
            <div className={styles.brandCluster}>
              <span className={styles.brandName}>{CONTACT.name}</span>
            </div>
            <p className={styles.footerTagline}>{CONTACT.tagline}</p>
            <div className={styles.footerStatus}>
              <span className={styles.greenRadiantPulse} />
              <span className={styles.footerLocation}>{CONTACT.location}</span>
            </div>
          </div>

          <div>
            <span className={styles.footerColLabel}>Core Stack</span>
            <div className={styles.arsenalBadgeFlow}>
              {CORE_STACK.map((tech) => (
                <span key={tech} className={styles.frostedBadge}>
                  {tech}
                </span>
              ))}
            </div>
          </div>

          <div className={styles.footerConnect}>
            <span className={styles.footerColLabel}>Connect</span>
            <div className={styles.footerSocialList}>
              {SOCIALS.map((social) => {
                const isExternal = social.href.startsWith('http');
                return (
                  <a
                    key={social.label}
                    className={styles.navPill}
                    href={social.href}
                    target={isExternal ? '_blank' : undefined}
                    rel={isExternal ? 'noopener noreferrer' : undefined}
                  >
                    <span className={styles.socialPrefix}>{social.prefix}</span>
                    {social.handle}
                  </a>
                );
              })}
            </div>
          </div>
        </div>

        <div className={styles.footerBottomBar}>
          <span>
            © {year} {CONTACT.name}. All rights reserved.
          </span>
        </div>
      </div>
    </footer>
  );
}
