<template>
  <b-container class="mt-5">
    <div class="text-center mb-5">
      <h2 class="font-weight-bold">Song Summaries</h2>
      <p class="text-muted">Manage your songs and their insights efficiently.</p>
    </div>
    <b-card class="mb-4 shadow-sm border-primary">
      <b-card-header class="bg-primary text-white">Add a New Song</b-card-header>
      <b-card-body>
        <b-alert
          v-if="successMessage"
          variant="success"
          class="mt-3"
          :show="5"
          dismissible
          @dismissed="successMessage = null"
        >
          {{ successMessage }}
        </b-alert>
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
        <b-form @submit.prevent="submitForm">
          <b-row>
            <b-col md="6">
              <b-form-group label="Title" label-for="title-input">
                <b-form-input
                  id="title-input"
                  v-model.lazy.trim="form.title"
                  placeholder="Enter song title"
                  required
                ></b-form-input>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group label="Author" label-for="author-input">
                <b-form-input
                  id="author-input"
                  v-model.lazy.trim="form.author"
                  placeholder="Enter author name"
                  required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          <b-button type="submit" variant="primary" block :disabled="isSubmitting">
            <span v-if="isSubmitting">
            <b-spinner small class="mr-2"></b-spinner> Submitting...
          </span>
            <span v-else>Add Song</span>
          </b-button>
        </b-form>
      </b-card-body>
    </b-card>
    <b-card class="shadow-sm border-info">
      <b-card-header class="bg-info text-white">Song List</b-card-header>
      <b-card-body>
        <b-table bordered hover sticky-header="500px" :items="songs" :fields="fields" show-empty>
          <template #cell(summary)="data">
            <span>{{ data.item.summary || "N/A" }}</span>
          </template>
          <template #cell(countries)="data">
            <span>{{ data.item.countries || "N/A" }}</span>
          </template>
        </b-table>
      </b-card-body>
    </b-card>
  </b-container>
</template>

<script>
import axios from "axios";
import {useAuthStore} from "@/stores/authStore";

export default {
  name: "SongsView",
  data() {
    return {
      fields: [
        {key: "id", label: "ID", sortable: true},
        {key: "title", label: "Title", sortable: false},
        {key: "author", label: "Author", sortable: false},
        {key: "summary", label: "Summary", sortable: false},
        {key: "countries", label: "Countries", sortable: false},
      ],
      songs: [],
      form: {
        title: "",
        author: "",
      },
      successMessage: null,
      errorMessage: null,
      isSubmitting: false,
    };
  },
  methods: {
    async submitForm() {
      this.isSubmitting = true;
      try {
        this.successMessage = null;
        this.errorMessage = null;
        const response = await axios.post(
          `${process.env.VUE_APP_BASE_API_URL}/api/songs`, this.form,
          {headers: this.authStore.getAuthHeader()}
        );
        this.successMessage = "Data submitted successfully!";
        this.form.title = "";
        this.form.author = "";

        const newSong = {
          id: response.data.id,
          title: response.data.title,
          author: response.data.author,
          summary: response.data.summary,
          countries: response.data.countries || "None",
        };
        this.songs.unshift(newSong);

      } catch (error) {
        this.errorMessage = error.response?.data?.message || "An error occurred while submitting the form.";
      } finally {
        this.isSubmitting = false;
      }
    },
  },
  mounted() {
    axios.get(`${process.env.VUE_APP_BASE_API_URL}/api/songs`, {headers: this.authStore.getAuthHeader()})
      .then(response => (this.songs.push(...response.data)))
  },
  created() {
    this.authStore = useAuthStore();
  },
};
</script>

<style scoped>
h2 {
  font-size: 2.5rem;
  color: #333;
}

.text-muted {
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

b-table {
  font-size: 1rem;
}
</style>
