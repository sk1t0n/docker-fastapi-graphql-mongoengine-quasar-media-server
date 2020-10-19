<template>
  <q-layout view="hHh LpR fff" class="background-dark">

    <q-header class="header-dark text-white">
      <div class="container">
        <q-toolbar>
          <q-toolbar-title class="quattrocento-font-bold header-logo">
            {{ logoText }}
          </q-toolbar-title>

          <div class="gt-md top-menu">
            <router-link
              v-for="item in topMenu"
              :key="item.title"
              :to="item.url"
            >
              {{ item.title }}
            </router-link>
          </div>

          <q-btn
            dense
            icon="menu"
            size="16px"
            aria-label="Menu"
            @click="leftDrawerOpen = !leftDrawerOpen"
            class="lt-lg btn-top-menu"
          />
        </q-toolbar>
      </div>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      side="left"
      content-class="drawer-dark flex items-center"
    >
      <q-list class="text-center">
        <q-item-label
          header
          class="text-white"
        >
          Menu
        </q-item-label>
        <MobileMenu
          v-for="item in topMenu"
          :key="item.title"
          :title="item.title"
          :url="item.url"
          class="text-white"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer class="footer-dark text-center quattrocento-font-regular">
      <a href="https://github.com">
        <q-avatar size="64px" class="social-btn">
          <q-img src="../assets/GitHub-Mark-64px.png" />
        </q-avatar>
      </a>
      <q-toolbar>
        <q-toolbar-title class="footer-logo">{{ logoText }}</q-toolbar-title>
      </q-toolbar>
      <p>Copyright &copy; 2020</p>
    </q-footer>
  </q-layout>
</template>

<script>
import MobileMenu from 'components/MobileMenu.vue'

const logoText = 'Media Server'
const topMenu = [
  {
    title: 'Home',
    url: '/'
  },
  {
    title: 'Add video',
    url: '/video/add'
  }
]

export default {
  name: 'MainLayout',
  components: { MobileMenu },
  data () {
    return {
      leftDrawerOpen: false,
      topMenu: topMenu,
      logoText: logoText,
      githubUrl: 'https://cdn.quasar.dev/img/parallax2.jpg'
    }
  }
}
</script>

<style lang="scss">
.container {
  margin: 0 auto;
}

@media screen and (max-width: 575px) {
  .container {
    width: 100%;
  }

  main {
    margin-top: 0.8rem;
    margin-bottom: 0.8rem;
  }
}

@media screen and (min-width: 576px) {
  .container {
    width: 540px;
  }

  main {
    margin-top: 1rem;
    margin-bottom: 1rem;
  }
}

@media screen and (min-width: 768px) {
  .container {
    width: 720px;
  }

  main {
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
  }
}

@media screen and (min-width: 992px) {
  .container {
    width: 960px;
  }

  main {
    margin-top: 2rem;
    margin-bottom: 2rem;
  }
}

@media screen and (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}

.background-dark {
  background-color: $background-dark;
}

.header-dark {
  background-color: $header-dark;
  height: 58px;
  padding-top: 4px;
}

.header-logo {
  font-size: 30px;
  margin-left: 2rem;
}

.top-menu a {
  margin-left: 10px;
  margin-right: 2rem;
}

.btn-top-menu {
  border: 1px solid rgba(255,255,255,.3);
  margin-right: 2rem;
}

.drawer-dark {
  background-color: $drawer-dark;

  .q-list {
    width: 100%;
  }
}

.footer-dark {
  background-color: $footer-dark;
  height: 230px;
  padding-top: 45px;
  font-size: 1rem;
}

.footer-logo {
  font-size: 1.7rem;
}

.social-btn {
  &:hover {
    background-color: $footer-social-hover;
  }
}

a {
  text-decoration: none;
  color: $top-menu-color;

  &:hover {
    color: $top-menu-hover-color;
  }
}
</style>
