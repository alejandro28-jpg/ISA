<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Para ti</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,500;1,600&family=Nunito:wght@400;600&display=swap">
<style>
:root{--bg:#2a0f1e;--bg2:#4a1a31;--paper:#fbeee6;--ink:#4a1a31;--rose:#e0607e;--gold:#e8b86d;
box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
html{height:100%;scroll-padding-top:env(safe-area-inset-top,0px)}
*,*::before,*::after{box-sizing:inherit}
body{margin:0;min-height:100%;background:radial-gradient(ellipse at 50% 20%,var(--bg2),var(--bg) 70%);color:var(--paper);font-family:Nunito,system-ui,sans-serif;display:flex;align-items:center;justify-content:center;overflow-x:hidden}
main{width:100%;max-width:420px;padding:24px;text-align:center;position:relative;z-index:1}
.seal{width:132px;height:132px;border-radius:50%;border:0;cursor:pointer;background:radial-gradient(circle at 35% 30%,#f08aa2,var(--rose) 55%,#a93a58);color:var(--paper);font:italic 600 44px/1 "Cormorant Garamond",Georgia,serif;box-shadow:0 10px 40px #e0607e55,inset 0 -6px 12px #0003;animation:beat 2.2s ease-in-out infinite}
.seal:focus-visible{outline:3px solid var(--gold);outline-offset:6px}
@keyframes beat{0%,100%{transform:scale(1)}50%{transform:scale(1.07)}}
.hint{margin-top:22px;color:#fbeee6bb;font-size:15px}
.card{display:none;background:var(--paper);color:var(--ink);border-radius:6px;padding:36px 28px;text-align:left;box-shadow:0 20px 60px #0007}
.card.on{display:block}
h1{font:italic 600 38px/1.1 "Cormorant Garamond",Georgia,serif;margin:0 0 18px}
.card p{font:italic 500 21px/1.5 "Cormorant Garamond",Georgia,serif;margin:0 0 14px;opacity:0;transform:translateY(6px);transition:opacity .9s,transform .9s}
.card p.show{opacity:1;transform:none}
.sign{font:600 15px Nunito,sans-serif!important;color:var(--rose)}
.h{position:fixed;bottom:-30px;color:var(--rose);pointer-events:none;animation:up linear forwards;z-index:0}
@keyframes up{to{transform:translateY(-115vh) rotate(20deg);opacity:0}}
@media (prefers-reduced-motion:reduce){.seal{animation:none}.h{display:none}.card p{transition:none}}
</style>
</head>
<body>
<main>
  <button class="seal" id="seal" aria-label="Abrir mensaje">♥</button>
  <p class="hint" id="hint">Toca el sello</p>
  <section class="card" id="card" aria-live="polite">
    <h1 id="title">Para ti</h1>
    <p>Hay días en que el mundo se pone ruidoso, y tú eres el lugar donde todo se calma.</p>
    <p>Gracias por reírte de mis chistes malos y por quedarte en los días difíciles.</p>
    <p>No necesito una fecha especial para recordártelo: me haces feliz.</p>
    <p class="sign">Te amo, mi princesa ♥</p>
  </section>
</main>
<script>
(function(){
  var name="";
  try{name=decodeURIComponent(location.hash.slice(1)).replace(/[^\p{L}\s-]/gu,"").trim();}catch(e){}
  if(name){document.getElementById("title").textContent="Para ti, "+name;}
  var seal=document.getElementById("seal"),card=document.getElementById("card"),hint=document.getElementById("hint");
  function heart(){
    var s=document.createElement("span");s.className="h";s.textContent="♥";
    s.style.left=Math.random()*100+"vw";s.style.fontSize=(12+Math.random()*22)+"px";
    s.style.animationDuration=(5+Math.random()*5)+"s";
    document.body.appendChild(s);setTimeout(function(){s.remove();},10500);
  }
  seal.addEventListener("click",function(){
    seal.style.display="none";hint.style.display="none";card.classList.add("on");
    var ps=card.querySelectorAll("p");
    ps.forEach(function(p,i){setTimeout(function(){p.classList.add("show");},400+i*1400);});
    for(var i=0;i<18;i++){setTimeout(heart,i*260);}
    setInterval(heart,900);
  });
})();
</script>
</body>
</html>
