<script setup>
import bridgeImg from "../assets/project-bridge.webp";
import vanhDaiImg from "../assets/Vanh-Dai-2-Tphcm.jpg";
import urbanBridgeImg from "../assets/project-urban-bridge.webp";

const projects = [
  {
    image: bridgeImg,
    title: "Lập dự án Khu công nghiệp Phú Chánh",
    location: "Bình Dương, Việt Nam",
    description: "Khảo sát chi tiết, lập quy hoạch và dự án đầu tư cho khu công nghiệp với hạ tầng kỹ thuật hoàn chỉnh.",
  },
  {
    image: vanhDaiImg,
    title: "Thiết kế Đường huyện ĐH.401",
    location: "Bình Dương, Việt Nam",
    description: "Thiết kế chi tiết đường huyện ĐH.401 với cải tiến hình học tuyến, an toàn giao thông và khả năng thông hành.",
  },
  {
    image: urbanBridgeImg,
    title: "Giám sát Đường trục chính huyện Tân Uyên",
    location: "Bình Dương, Việt Nam",
    description: "Giám sát thi công toàn diện đường trục chính huyện Tân Uyên, đảm bảo chất lượng và tiến độ dự án.",
  },
];
</script>

<template>
  <section id="projects" class="section">
    <div class="container">
      <h2 class="section-title">Dự án tiêu biểu</h2>
      <p class="section-subtitle">Một số dự án khảo sát và thiết kế gần đây thể hiện định hướng của chúng tôi về kết cấu bền vững và hành lang giao thông hiệu quả.</p>

      <div class="projects-grid">
        <article v-for="project in projects" :key="project.title" class="project-card">
          <img :src="project.image" :alt="project.title" loading="lazy" />
          <div class="project-body">
            <h3>{{ project.title }}</h3>
            <p class="project-location">{{ project.location }}</p>
            <p>{{ project.description }}</p>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.projects-grid {
  margin-top: 1.7rem;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.project-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow);
}

.project-card img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  display: block;
}

.project-body {
  padding: 1.05rem;
}

.project-body h3 {
  font-family: "Be Vietnam Pro", "Segoe UI", sans-serif;
  text-transform: uppercase;
  color: var(--brand-deep);
  letter-spacing: 0.03em;
  font-size: 1.05rem;
  line-height: 1.3;
}

.project-location {
  margin: 0.4rem 0 0.65rem;
  color: var(--accent);
  font-weight: 700;
  font-size: 0.9rem;
}

.project-body p {
  margin: 0;
  color: var(--muted);
  font-size: 0.92rem;
  line-height: 1.5;
}

@media (max-width: 1000px) {
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 620px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }

  .project-card img {
    height: 200px;
  }
}
</style>
