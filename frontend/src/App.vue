<template>
  <div>
    <Header></Header>
    <b-container class="content">
      <RouterView/>
    </b-container>
    <Footer></Footer>
  </div>
</template>
<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: 'App',
  components: {
    Header,
    Footer,
  },
  mounted() {
    const script = document.createElement("script");
    script.src = "https://kit.fontawesome.com/090385f77a.js";
    document.body.appendChild(script);
  },
}
</script>

<style scoped>
.content {
  margin-top: 5rem;
  padding-bottom: 5rem;
}
</style>
