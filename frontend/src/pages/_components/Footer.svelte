<footer>
  <img src="white_logo.svg" class="logo-white" alt="logo-white"/>
  <div class="content">
    <div class="column-block">
      <h3>О НАС</h3>
      <ul>
        <a href="https://www.patreon.com/commondatateam">
          <li>поддержать проект</li>
        </a>
        <a href="/privacy">
          <li>пользовательское соглашение</li>
        </a>
      </ul>
    </div>
    <div class="column-block">
      <h3>СВЯЗАТЬСЯ С НАМИ</h3>
      <ul>
        <a href="mailto:help@commondata.ru">
          <li>help@commondata.ru</li>
        </a>
      </ul>
    </div>
    <div class="column-block">
      <h3>СОЦСЕТИ</h3>
      <ul>
        <a href="https://github.com/tpofd/common-data-app">
          <li>github</li>
        </a>
      </ul>
    </div>
  </div>
</footer>

<style>
  footer {
    display: flex;
    bottom: 0;
    padding: 5% 0;
    margin-top: 5%;
    width: 100%;
    background: #282828;
    align-items: stretch;
  }

  .content {
    display: flex;
    justify-content: space-around;
    flex: 1 1;
  }

  .column-block {
    margin-right: 10%;
  }

  .logo-white {
    max-width: 285px;
    margin-right: 15%;
    flex: 0 0 0;
    margin-left: 5%;
  }

  h3 {
    color: #F9F9F9;
    --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
    font-family: "Helvetica Neue";
  }

  li {
    list-style-type: none;
  }

  ul {
    padding: 0;
  }

  a {
    color: #BDBDBD;
    font-family: "Helvetica Norm";
    --plain-font-size: calc(12px + (14 - 12) * ((100vw - 300px) / (1440 - 300)));
    text-decoration: none;
  }

  a:hover {
    color: #1355FF;
  }

  @media (min-width: 2000px) {
    footer {
      justify-content: left;
    }

    .content {
      flex: 0 0 300px;
    }

    .logo-white {
      margin-right: 5%;
    }

    .column-block {
      flex:  0 0;
    }
  }

  @media (max-width: 1270px) {

    footer {
      flex-direction: column;
    }

    .logo-white {
      max-width: 200px;
      margin-left: 5%;
      margin-bottom: 5%;
    }

    .column-block {
      padding-left: 5%;
    }
  }

  @media (max-width: 700px) {
    .content {
      flex-direction: column;
    }
  }
</style>