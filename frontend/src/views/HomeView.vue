<script>

export default {
  name: "HomeView"
}
</script>
<template>
  <div>
    <b-jumbotron header-tag="h6" bg-variant="light" text-variant="dark" border-variant="info" class="mt-5 text-center">
      <h3>Experience the Power of AI with LLM</h3>Experience the Power of AI with LLM
      <template #lead>
        Revolutionizing Your Workflows with Advanced Language Intelligence
      </template>
      <hr class="my-4">
      <p>
        Our LLM-powered app leverages cutting-edge AI to streamline processes, enhance productivity, and deliver smarter
        solutions tailored to your needs.
      </p>
    </b-jumbotron>
    <b-row>
      <b-col md="6" class="mb-4">
        <b-card class="h-100 shadow-sm border-primary">
          <b-card-header class="bg-primary text-white text-center">
            Features
          </b-card-header>
          <b-card-body>
            <ul class="list-unstyled">
              <li>
                <i class="fas fa-lock text-primary"></i> Authentication and authorization
              </li>
              <li>
                <i class="fas fa-user-circle text-primary"></i> Profile overview
              </li>
              <li>
                <i class="fas fa-music text-primary"></i> Analyze the song title and author and provide a quick summary
              </li>
              <li>
                <i class="fas fa-globe text-primary"></i> Highlight countries mentioned in the song
              </li>
              <li>
                <i class="fas fa-database text-primary"></i> Handling repetitive and exact requests by caching responses
                and optimizing LLM usage
              </li>
            </ul>
          </b-card-body>
        </b-card>
      </b-col>
      <b-col md="6" class="mb-4">
        <b-card class="h-100 shadow-sm border-info">
          <b-card-header class="bg-info text-white">
            About the Author
          </b-card-header>
          <b-card-body class="text-center">
            <p>
              <i class="fas fa-user text-info"></i>
              Skilled in building robust server-side applications using Python, Node.js, and SQL/NoSQL databases.
            </p>
            <p>
              <i class="fas fa-code text-info"></i> Experienced in crafting interactive interfaces with Vue.js,
              React, and modern JavaScript standards.
            </p>
            <p>
              <i class="fas fa-users-cog text-info"></i> Proficient in Agile methodologies and leading teams to
              deliver high-quality software solutions.
            </p>
            <p>
              <i class="fas fa-server text-info"></i> Expertise in AWS, Docker, Kubernetes, and setting up
              scalable, fault-tolerant systems.
            </p>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<style scoped>
h2 {
  font-size: 2rem;
  color: #333;
}

ul li {
  margin-bottom: 0.75rem;
  font-size: 1.1rem;
}

p {
  font-size: 1.2rem;
  color: #555;
}
</style>
