<template>
  <b-container class="d-flex align-items-center justify-content-center vh-70">
    <b-card
      class="text-center"
      bg-variant="light"
      border-variant="warning"
      header="Logout Confirmation"
      header-bg-variant="warning"
      header-text-variant="light"
    >
      <b-card-body>
        <p>Are you sure you want to log out?</p>
        <b-button variant="danger" class="mr-2" @click="confirmLogout">
          Confirm
        </b-button>
        <b-button variant="secondary" @click="cancelLogout">
          Cancel
        </b-button>
      </b-card-body>
    </b-card>
  </b-container>
</template>

<script>
import {useAuthStore} from "@/stores/authStore";

export default {
  name: "Logout",
  methods: {
    confirmLogout() {
      this.authStore.logout()
      this.$router.push('/')
    },
    cancelLogout() {
      this.$router.go(-1)
    },
  },
  created() {
    this.authStore = useAuthStore();
  },
};
</script>

<style scoped>
.vh-70 {
  min-height: 50vh;
}
</style>
