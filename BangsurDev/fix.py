import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. SMK Assalaam Logo
old_smk = r'''<div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-3 border-b border-brand-black/10">
                        <div>
                            <h4 class="text-sm font-bold uppercase tracking-wider text-brand-blue">SMK Assalaam Bandung</h4>
                            <p class="text-[10px] font-mono text-stone-500 uppercase">PKL Internal — Website Developer</p>
                        </div>'''
new_smk = r'''<div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-3 border-b border-brand-black/10">
                        <div class="flex items-center gap-3">
                            <img src="./img/smkassalaambandung.png" alt="SMK Assalaam" class="h-8 w-auto max-w-[4rem] object-contain">
                            <div>
                                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-blue">SMK Assalaam Bandung</h4>
                                <p class="text-[10px] font-mono text-stone-500 uppercase">PKL Internal — Website Developer</p>
                            </div>
                        </div>'''
content = content.replace(old_smk, new_smk)

# 2. Hero photo
content = content.replace('src="im.png"', 'src="./img/im.png"')

# 3. Remove text from tech pills
# The regex finds <span class="tech-pill"...> up to the last > before </span>, and removes the text
content = re.sub(r'(<span class="tech-pill"[^>]*>.*?)(>[^<]*?)(</span>)', r'\1>\3', content, flags=re.DOTALL)

# Also remove gap, padding from tech-pill so the logos look centered if they had paddings for text
# <span class="tech-pill" style="font-size:9px; padding: 3px 8px 3px 5px; gap: 4px;"> -> remove style?
# Tech pills with inline style:
content = re.sub(r'style="[^"]*padding[^"]*"', '', content)
# Just to make sure tech pills look good without text, we can modify the .tech-pill CSS or just add w-6 h-6 to imgs?
# Wait, they already have width/height or flex.
# Let's clean up any empty spans just in case.
content = content.replace('<span class="tech-pill"></span>', '')

# 4. Project images "full"
# Project 1: Siruang
content = content.replace(
    '<div class="relative aspect-video bg-brand-light border-b-2 border-brand-black overflow-hidden">\n                    <img class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500"\n                         src="./img/siruang_web.png"',
    '<div class="relative bg-brand-light border-b-2 border-brand-black overflow-hidden">\n                    <img class="w-full h-auto grayscale group-hover:grayscale-0 transition-all duration-500"\n                         src="./img/siruang_web.png"'
)
# Project 2: RumahKos
content = content.replace(
    '<div class="relative aspect-video bg-brand-light border-b-2 border-brand-black overflow-hidden">\n                    <img class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500"\n                         src="./img/rumahkos_web.png"',
    '<div class="relative bg-brand-light border-b-2 border-brand-black overflow-hidden">\n                    <img class="w-full h-auto grayscale group-hover:grayscale-0 transition-all duration-500"\n                         src="./img/rumahkos_web.png"'
)
# Project 3: IndoTeknisi Web
content = content.replace(
    '<div class="relative aspect-video lg:aspect-[21/9] bg-brand-light border-b-2 border-brand-black overflow-hidden">\n                <img class="w-full h-full object-cover object-top grayscale group-hover:grayscale-0 transition-all duration-500"\n                     src="./img/indoteknisi_web.png"',
    '<div class="relative bg-brand-light border-b-2 border-brand-black overflow-hidden">\n                <img class="w-full h-auto grayscale group-hover:grayscale-0 transition-all duration-500"\n                     src="./img/indoteknisi_web.png"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixes applied successfully!")
