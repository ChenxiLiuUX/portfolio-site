import re, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
css = open('styles.css').read()
pages = [("index","Chenxi Liu — Product designer"),("case-parallel-chatbot","Parallel chatbot — Chenxi Liu"),
         ("case-parallel-admin","Parallel admin tool — Chenxi Liu"),("case-maya-migrate","Maya Migrate — Chenxi Liu"),
         ("case-shopify-audits","Shopify UX audits — Chenxi Liu")]
def links(h):
    h = re.sub(r'href="index\.html#([\w-]+)"', r'href="#/index/\1"', h)
    h = h.replace('href="index.html"', 'href="#/"')
    return re.sub(r'href="(case-[\w-]+)\.html"', r'href="#/\1"', h)
blocks = []
for name, title in pages:
    main = open(f'{name}.html').read().split('<main id="main" class="wrap">',1)[1].split('</main>',1)[0]
    if name != "index":
        main = re.sub(r'\bid="([\w-]+)"', lambda m: f'id="{name}-{m.group(1)}"', main)
        main = re.sub(r'aria-labelledby="([\w-]+)"', lambda m: f'aria-labelledby="{name}-{m.group(1)}"', main)
    blocks.append(f'<div class="page" data-page="{name}" data-title="{title}" hidden>{links(main)}</div>')
idx = open('index.html').read()
header = links(open('case-parallel-chatbot.html').read().split('<header class="site-header">',1)[1].split('</header>',1)[0])
footer = idx.split('<footer class="site-footer">',1)[1].split('</footer>',1)[0]
head = idx.split('<link rel="stylesheet" href="styles.css">',1)[0]
script = r'''<script>
(function () {
  const pages = document.querySelectorAll('.page');
  const navLinks = document.querySelectorAll('.site-nav a');
  function route() {
    const h = location.hash;
    if (h && !h.startsWith('#/')) return;
    const parts = h.replace(/^#\//, '').split('/').filter(Boolean);
    let name = parts[0] || 'index';
    if (!document.querySelector('.page[data-page="' + name + '"]')) name = 'index';
    pages.forEach(p => { p.hidden = p.dataset.page !== name; });
    const page = document.querySelector('.page[data-page="' + name + '"]');
    document.title = page.dataset.title;
    document.body.dataset.page = name;
    navLinks.forEach(a => a.removeAttribute('aria-current'));
    if (name !== 'index') { const w = document.querySelector('.site-nav a[href="#/index/work"]'); if (w) w.setAttribute('aria-current', 'page'); }
    const el = parts[1] && document.getElementById(parts[1]);
    if (el) el.scrollIntoView(); else window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', route);
  route();
})();
</script>'''
out = (head + '<style>\n' + css + '\n</style>\n</head>\n<body>\n<a class="skip-link" href="#main">Skip to content</a>\n'
       + f'<header class="site-header">{header}</header>\n<main id="main" class="wrap" tabindex="-1">\n' + "".join(blocks)
       + f'\n</main>\n<footer class="site-footer">{footer}</footer>\n' + script + '\n</body>\n</html>\n')
import base64
def inline_images(h):
    def rep(m):
        p = m.group(1)
        data = base64.b64encode(open(p,'rb').read()).decode()
        return f'src="data:image/jpeg;base64,{data}"'
    return re.sub(r'src="(images/[\w.-]+\.jpg)"', rep, h)
out = inline_images(out)
open('portfolio-preview.html','w').write(out)
print('bundled', len(out))
