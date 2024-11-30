<template>
  <b-container class="mt-5">
    <div class="text-center mb-5">
      <h2 class="font-weight-bold">Technologies We Used</h2>
      <p class="text-muted">A robust stack driving innovative and scalable solutions.</p>
    </div>
    <b-row>
      <b-col md="3" class="mb-4">
        <b-card class="h-100 shadow-sm border-primary">
          <b-card-header class="bg-primary text-white text-center">Frontend</b-card-header>
          <b-card-body>
            <ul class="list-unstyled text-center">
              <li><i class="fas fa-code text-primary"></i> JavaScript</li>
              <li><i class="fas fa-laptop-code text-primary"></i> Vue 2</li>
              <li><i class="fas fa-palette text-primary"></i> Bootstrap 4</li>
            </ul>
          </b-card-body>
        </b-card>
      </b-col>
      <b-col md="3" class="mb-4">
        <b-card class="h-100 shadow-sm border-success">
          <b-card-header class="bg-success text-white text-center">Backend</b-card-header>
          <b-card-body>
            <ul class="list-unstyled text-center">
              <li><i class="fas fa-terminal text-success"></i> Python 3.11</li>
              <li><i class="fas fa-server text-success"></i> Django 4.2</li>
              <li><i class="fas fa-link text-success"></i> DRF 3.14</li>
              <li><i class="fas fa-database text-success"></i> PostgreSQL 15.5</li>
            </ul>
          </b-card-body>
        </b-card>
      </b-col>
      <b-col md="3" class="mb-4">
        <b-card class="h-100 shadow-sm border-info">
          <b-card-header class="bg-info text-white text-center">Infrastructure</b-card-header>
          <b-card-body>
            <ul class="list-unstyled text-center">
              <li><i class="fas fa-docker text-info"></i> Docker & Docker Compose</li>
              <li><i class="fas fa-cloud text-info"></i> Digital Ocean Droplets</li>
              <li><i class="fas fa-database text-info"></i> DO Storage</li>
            </ul>
          </b-card-body>
        </b-card>
      </b-col>
      <b-col md="3" class="mb-4">
        <b-card class="h-100 shadow-sm border-warning">
          <b-card-header class="bg-warning text-dark text-center">ML & AI</b-card-header>
          <b-card-body>
            <ul class="list-unstyled text-center">
              <li><i class="fas fa-brain text-warning"></i> OpenAI GPT API</li>
              <li><i class="fas fa-code text-warning"></i> Python LLM</li>
              <li><i class="fas fa-server text-warning"></i> Self-hosted & Remote Models</li>
            </ul>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "AboutView",
};
</script>

<style scoped>
h2 {
  font-size: 2.5rem;
  color: #333;
}

.text-muted {
  font-size: 1rem;
}

ul li {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}
</style>
