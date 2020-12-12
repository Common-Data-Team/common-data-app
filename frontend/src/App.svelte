<script>
  import {Router} from "@roxi/routify";
  import {routes} from "../.routify/routes";
  import {setContext} from "svelte";

  // TODO Выстроить условие среды
  // if (true) {
  //   setContext('apiUrl', 'http://localhost:8000/');
  //   setContext('selfUrl', 'http://localhost:5000/');
  // } else {
  //   setContext('apiUrl', 'https://backend.commondata.ru/');
  //   setContext('selfUrl', 'https://commondata.ru/');
  // }
  setContext('apiUrl', 'https://backend.commondata.ru/');
  setContext('selfUrl', 'http://localhost:5000/');
</script>

<svelte:head>
  <link rel="shortcut icon" href="/flavicon.svg" type="image/svg+xml">
  <!-- Yandex.Metrika counter -->
  <script type="text/javascript">
    (function (m, e, t, r, i, k, a) {
      m[i] = m[i] || function () {
        (m[i].a = m[i].a || []).push(arguments)
      };
      m[i].l = 1 * new Date();
      k = e.createElement(t), a = e.getElementsByTagName(t)[0], k.async = 1, k.src = r, a.parentNode.insertBefore(k, a)
    })
    (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

    ym(68407234, "init", {
      clickmap: true,
      trackLinks: true,
      accurateTrackBounce: true
    });
  </script>
  <noscript>
    <div><img src="https://mc.yandex.ru/watch/68407234" style="position:absolute; left:-9999px;" alt=""/></div>
  </noscript>
  <!-- /Yandex.Metrika counter -->
</svelte:head>

<style global>
  @import "../assets/global.css";

  #routify-app {
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
  }
</style>

<Router {routes}/>
