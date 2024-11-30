import {defineStore} from 'pinia';
import axios from "axios";

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    isAuthenticated: false,
    errorLoginFailed: null,
  }),
  actions: {
    login(payload) {
      this.errorLoginFailed = null;
      return axios.post(`${process.env.VUE_APP_BASE_API_URL}/api/users/login/`, payload)
        .then(response => {
          this.user = response.data;
          this.isAuthenticated = true;
        })
        .catch((error) => {
          this.errorLoginFailed = error.message
        })
    },
    logout() {
      return axios.post(`${process.env.VUE_APP_BASE_API_URL}/api/users/logout/`)
        .then(response => {
          this.isAuthenticated = false;
          this.user = null;
        })
        .catch(e => {
          console.log(e)
        })
    },
    getAuthHeader() {
      return {"Authorization": `Token ${this.user?.token}`}
    }
  },
  getters: {
    isLoggedIn: (state) => state.isAuthenticated,
    getUser: (state) => state.user,
    getErrorLoginFailed: (state) => state.errorLoginFailed,
  },
});
