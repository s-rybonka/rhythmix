<template>
  <b-navbar toggleable="lg" type="dark" variant="info" fixed="top">
    <b-navbar-brand to="/">
      <img src="../../public/img/Logo.png" alt="Kitten" class="rounded-circle" width="35" height="35">
      Rhythmix
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/" :class="{ active: activeItem === 'home' }" @click="setActive('home')">
          Home
        </b-nav-item>
        <b-nav-item to="/about" :class="{ active: activeItem === 'about' }" @click="setActive('about')">
          About
        </b-nav-item>
        <b-nav-item to="/songs" v-if="isLoggedIn" :class="{ active: activeItem === 'songs' }"
                    @click="setActive('songs')">
          Songs
        </b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <template #button-content>
            <em v-if="isLoggedIn">Welcome, {{ user.full_name }}</em>
            <em v-else>Anonymous Account</em>
          </template>
          <b-dropdown-item to="/profile" v-if="isLoggedIn">Profile</b-dropdown-item>
          <b-dropdown-item v-if="!isLoggedIn">
            <b-dropdown-item to="/login">Login</b-dropdown-item>
          </b-dropdown-item>
          <b-dropdown-item to="/logout" v-else>Logout</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<script>
import {useAuthStore} from "@/stores/authStore";

export default {
  name: "Header",
  data() {
    return {
      activeItem: "home",
    };
  },
  methods: {
    setActive(item) {
      this.activeItem = item;
    },
  },
  computed: {
    isLoggedIn() {
      return this.authStore.isLoggedIn;
    },
    user() {
      return this.authStore.getUser;
    },
  },
  created() {
    this.authStore = useAuthStore();
  },
}
</script>
