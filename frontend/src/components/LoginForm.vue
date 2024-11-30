<template>
  <b-container class="d-flex align-items-center justify-content-center vh-70">
    <b-card title="User Login" class="w-50 mx-auto">
      <b-form @submit.prevent="handleLogin">
        <b-alert
            v-if="errorMessage"
            variant="danger"
            class="mt-3"
            :show="5"
            dismissible
            @dismissed="errorMessage = null"
        >
          {{ errorMessage }}
        </b-alert>
        <b-form-group label="Email" label-for="email">
          <b-form-input
              id="email"
              v-model="email"
              type="email"
              placeholder="Enter your email"
              required
          ></b-form-input>
        </b-form-group>
        <b-form-group label="Password" label-for="password">
          <b-form-input
              id="password"
              v-model="password"
              type="password"
              placeholder="Enter your password"
              required
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="info" block>Login</b-button>
      </b-form>
    </b-card>
  </b-container>
</template>

<script>
import {useAuthStore} from "@/stores/authStore";


export default {
  name: 'LoginForm',
  data() {
    return {
      email: '',
      password: '',
      errorMessage: null,
    };
  },
  methods: {
    async handleLogin() {
      this.errorMessage = null;

      await this.authStore.login({
        email: this.email,
        password: this.password,
      });

      if (this.authStore.getErrorLoginFailed) {
        this.errorMessage = this.authStore.getErrorLoginFailed
      } else {
        await this.$router.push('/profile')
      }
    },
  },
  created() {
    this.authStore = useAuthStore();
  },
};
</script>

<style scoped>
.vh-70 {
  min-height: 70vh;
}
</style>
