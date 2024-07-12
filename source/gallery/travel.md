---
title: Travel 
date: 2024-07-10 00:47:00
single_column: true
---

<div class="trm-card">
{% galleryGroup %}
  <img class="drawing" src="https://s2.loli.net/2022/08/05/Qof4unCSsgJdMIR.jpg" alt="Glendalough" title="Glendalough,Ireland &#10;2021-10-10" >
   <img class="drawing" src="https://s2.loli.net/2022/08/05/4BbEZHVXPnpR1Fz.jpg" alt="Giant Causeway " title="Giant Causeway, Northern Ireland &#10;2021-12-26" >
   <img class="drawing" src="https://s2.loli.net/2022/08/05/sD2kUZ8Ad4IcMXV.jpg" title="Belfast Cityhall, Northern Ireland" >
   <img class="drawing" src="https://s2.loli.net/2022/08/05/H4Zq6MD9hd7wkgQ.jpg" title="Maynooth University, Ireland" >
   <img class="drawing" src="https://s2.loli.net/2022/08/05/JfoUqKOPHuWFnN8.jpg" title="Powerscourt Gardens, Ireland" >
   <img class="drawing" src="https://s2.loli.net/2023/09/22/PUXIHfVABeq7nKy.jpg" title="Puy de Dôme, France" >
   <img class="drawing" src="https://s2.loli.net/2023/12/03/GKl2DL4p1teRurX.jpg" title="Le Crozet, France" >
   <img class="drawing" src="https://s2.loli.net/2023/12/04/8H1IFuOmS3fdgkw.jpg" title="Le Crozet, France" >
   <img class="drawing" src="https://s2.loli.net/2023/12/30/2zROnfAuIogQkxa.jpg" title="Sveti Stefan, Montenegro" >
   <img class="drawing" src="https://s2.loli.net/2023/12/30/fR3qv1XMKwOhC9Z.jpg" title="Budva, Montenegro" >
   <img class="drawing" src="https://s2.loli.net/2023/12/31/s523twiVEdHTzQ9.jpg" title="Perast, Montenegro" >
   <img class="drawing" src="https://s2.loli.net/2024/04/11/2HA8ZoPBTxXeg6c.jpg" title="Venice, Italy" >
   <img class="drawing" src="https://s2.loli.net/2024/07/13/J3wflcHOeh2km7K.jpg" title="Venice, Italy" >
   <img class="drawing" src="https://s2.loli.net/2024/07/13/dos1YaJ92LP4Qnl.jpg" title="Pisa, Italy" >
   <img class="drawing" src="https://s2.loli.net/2024/07/13/VQ2LkNOHfCUzWMt.jpg" title="Dublin, Ireland" >
   <img class="drawing" src="https://s2.loli.net/2024/07/13/IMAW3XmdC8rLHxV.jpg" title="Prague, Czech Republic" >
   <img class="drawing" src="https://s2.loli.net/2024/07/13/9ypiQT5aRYJmUBr.jpg" title="Vienna, Austria" >
   
{% endgalleryGroup %}
</div>


<script>
  document.addEventListener('DOMContentLoaded', function() {
    var container = document.querySelector('.trm-card');
    var images = Array.from(container.querySelectorAll('img.drawing'));
    
    for (let i = images.length - 1; i > 0; i--) {
      let j = Math.floor(Math.random() * (i + 1));
      [images[i].src, images[j].src] = [images[j].src, images[i].src];
      [images[i].alt, images[j].alt] = [images[j].alt, images[i].alt];
      [images[i].title, images[j].title] = [images[j].title, images[i].title];
    }
  });
</script>