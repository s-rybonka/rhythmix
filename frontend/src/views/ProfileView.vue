<template>
  <b-container class="mt-5">
    <b-row>
      <b-col md="4" class="mb-4">
        <b-card>
          <b-card-img
            src="https://via.placeholder.com/150"
            alt="Profile Picture"
            class="rounded-circle mx-auto d-block"
            style="width: 150px; height: 150px;"
          ></b-card-img>
          <b-card-body class="text-center">
            <b-card-title>{{ profile.full_name }}</b-card-title>
            <b-card-sub-title>{{ profile.job_title }}</b-card-sub-title>
            <p class="mt-2">
              {{ profile.short_description }}
            </p>
          </b-card-body>
        </b-card>
      </b-col>
      <b-col md="8">
        <b-card>
          <b-card-body>
            <b-card-title>About Me</b-card-title>
            <p>
              {{ profile.description }}
            </p>
            <b-card-title class="mt-4">Contact Information</b-card-title>
            <b-list-group>
              <b-list-group-item><strong>Email:</strong> {{ profile.email }}</b-list-group-item>
              <b-list-group-item><strong>Phone:</strong> {{ profile.phone_number }}</b-list-group-item>
              <b-list-group-item><strong>Location:</strong> {{ profile.location }}</b-list-group-item>
            </b-list-group>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
    <b-row class="mt-4">
      <b-col>
        <b-card>
          <b-card-body>
            <b-card-title>Skills</b-card-title>
            <p>
              My technical expertise spans across various domains, including:
            </p>
            <b-badge variant="info" class="mr-2" v-for="item in profile.skills_list">
              {{ item }}
            </b-badge>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios";
import {useAuthStore} from "@/stores/authStore";

export default {
  name: "Profile",
  data() {
    return {
      profile: {},
    };
  },
  mounted() {
    const store = useAuthStore()
    axios.get(`${process.env.VUE_APP_BASE_API_URL}/api/users/profile/`, {headers: store.getAuthHeader()}
    ).then(response => (this.profile = response.data))
  }
}
</script>
