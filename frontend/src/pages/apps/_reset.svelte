<script>
import { url, isActive } from '@roxi/routify';
</script>

<main>
    <a href="/" class="return-link">
    <div class="return">
      <p class="arrow">→</p>
      <div class="chaif">Главная</div>
    </div>
  </a>
    <div class="content">
    <slot />
    <div class="right-menu">
          <a href={$url('./:user_id/index')} class:current={$isActive('./:user_id/index')}>Информация</a>
          <a href='/'>Достижения</a>
          <a href={$url('./:user_id/projects')} class:current={$isActive('./:user_id/projects')}>Мои проекты</a>
      </div>
    </div>
</main>

<style>
    main {
        width: 100%;
    }
    .right-menu {
        position: absolute;
        top: 0;
        right: 5%;
  }

  .right-menu a {
    font-family: "Helvetica Norm";
    font-size: 20px;
    margin: 7px;
    display: flex;
    flex-direction: column;
    text-align: right;
    text-decoration: none;
  }
  .current {
      text-decoration: underline !important;
  }
    .return {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    margin-top: 2%;
    margin-bottom: 2%;
    margin-left: 5%;
  }

  .return-link {
    text-decoration: none;
  }

  .return-link:hover {
    color: #282828;
  }

   .arrow {
    font-family: "SF Pro Display";
    font-size: 32px;
    text-align: center;

    color: #282828;
    transform: rotate(-180deg);
    align-self: center;
    margin-right: 2%;
  }

  .chaif {
    position: static;
    width: 77px;
    height: 24px;
    left: 53px;
    top: 7px;
    font-family: "Helvetica Norm";
    font-style: normal;
    font-weight: normal;
    line-height: 24px;
    display: flex;
    align-items: center;
    flex: none;
    order: 1;
    align-self: center;
    flex-grow: 0;
    margin: 16px 0px;
  }
    .content {
        position: relative;
    }
    @media (min-width: 1800px) {
        main {
            width: 1500px;
        }
    }
</style>
