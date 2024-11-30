<template>
  <b-navbar toggleable="lg" type="dark" variant="info" fixed="top">
    <b-navbar-brand href="">Rhythmix</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item to="/about">About</b-nav-item>
        <b-nav-item to="/songs" v-if="isLoggedIn">Songs</b-nav-item>
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
