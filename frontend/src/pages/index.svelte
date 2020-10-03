<script>
 
</script>

<main>
    <img src="/logo.svg" class="logo-img" alt="logo">
</main>

<footer>
    <div class="footer-flex-holder">
        <div class="foot-one">
            <img src="/images/touch-icons/logo-white.png" alt="logo-white" class="svg-color">
        </div>
        <div class="foot-two">Второй блок</div>
        <div class="foot-three">
            <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "</p>
        </div>
        <div class="foot-four">Четвертый блок</div>
        <div class="foot-five">Пятый блок</div>
    </div>
</footer>

<style>
.foot-one {
    fill: #F9F9F9;
}
footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 160px; /* Фиксированная высота необходима для прижатия */
    padding: 30px 0;
    background: linear-gradient(to bottom,#262626,#1d1d1d);
}
.footer-flex-holder {
   display: -ms-flexbox;	
   display: -webkit-flex;	
   display: -webkit-box;	
   display: flex;
   -ms-flex-pack: justify;	
   -webkit-justify-content: space-between;	
   -webkit-box-pack: justify;	
   justify-content: space-between;
}
footer .foot-one {
   background: #2c68a3;
   flex: 0 0 250px; /* Данный блок имеет конктретный размер и не меняет его */
}
footer .foot-two {
   flex: 1 1 0%;
   background: #2ca3a3;
}
footer .foot-three {
   flex: 1 1 0%;
   background: #2ca363;
}
footer .foot-four {
   flex: 1 1 0%;
   background: #55a32c;
}
footer .foot-five {
   flex: 1 1 0%;
   background: #a39a2c;
}
@media (max-width: 768px) {
    /* Размещаем блоки в подвале вертикально */
    .footer-flex-holder {
        flex-direction: column;
    }
    .footer-flex-holder .foot-one {
        flex: 1 1 0%;
    }
}
</style>