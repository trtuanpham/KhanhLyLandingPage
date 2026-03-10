<script setup>
import HeroSection from "./components/HeroSection.vue";
import AboutSection from "./components/AboutSection.vue";
import ServicesSection from "./components/ServicesSection.vue";
import ProjectsSection from "./components/ProjectsSection.vue";
import ContactSection from "./components/ContactSection.vue";
</script>

<template>
  <div class="page-wrap">
    <header class="site-header">
      <div class="container nav-bar">
        <a class="brand" href="#top">CTY TNHH TƯ VẤN KHẢO SÁT<br />VÀ THIẾT KẾ XÂY DỰNG KHÁNH LY</a>
        <nav class="nav-links">
          <a href="#about">Giới thiệu</a>
          <a href="#services">Dịch vụ</a>
          <a href="#projects">Dự án</a>
          <a href="#contact">Liên hệ</a>
        </nav>
      </div>
    </header>

    <main id="top">
      <HeroSection />
      <AboutSection />
      <ServicesSection />
      <ProjectsSection />
      <ContactSection />
    </main>

    <footer class="site-footer">
      <div class="container">
        <p>© {{ new Date().getFullYear() }} CTY TNHH TƯ VẤN KHẢO SÁT VÀ THIẾT KẾ XÂY DỰNG KHÁNH LY. Đồng hành cùng quy hoạch và thiết kế hạ tầng bền vững.</p>
      </div>
    </footer>
  </div>
</template>
