<script setup>
const documents = [
  { name: "Chứng nhận đào tạo", file: new URL("../assets/scans/CHỨNG NHẬN ĐÀO TẠO.pdf", import.meta.url).href },
  { name: "Giấy chứng nhân hoàn thành", file: new URL("../assets/scans/GIẤY CHỨNG NHÂN HOÀN THÀNH.pdf", import.meta.url).href },
  { name: "Giấy đăng ký kinh doanh", file: new URL("../assets/scans/GIẤY ĐĂNG KÝ KINH DOANH.pdf", import.meta.url).href },
  { name: "Mẫu số 01 - Thông tư năng lực đủ điều kiện hoạt động thí nghiệm", file: new URL("../assets/scans/MẪU SỐ 01 TT NĂNG LỰC ĐỦ ĐK HĐỘNG THÍ NGHIỆM.pdf", import.meta.url).href },
  { name: "Mẫu số 02 - Công bố thông tư dừng hoạt động thí nghiệm", file: new URL("../assets/scans/MẪU SỐ 02 CÔNG BỐ TT DỪNG HOẠT ĐỘNG THÍ NGHIỆM.pdf", import.meta.url).href },
];
</script>

<template>
  <section id="documents" class="section documents">
    <div class="container">
      <h2 class="section-title">Tài liệu</h2>
      <p class="section-subtitle">Giấy chứng nhận, giấy phép kinh doanh và các tài liệu liên quan đến năng lực hoạt động của công ty</p>

      <div class="documents-content">
        <ul class="documents-list">
          <li v-for="(doc, index) in documents" :key="index" class="document-item">
            <div class="doc-info">
              <i class="material-icons doc-icon">description</i>
              <span class="doc-name">{{ doc.name }}</span>
            </div>
            <a :href="doc.file" download :title="`Tải ${doc.name}`" class="download-btn">
              <i class="material-icons">download</i>
              Tải xuống
            </a>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>
.documents {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.74) 0%, rgba(226, 235, 241, 0.86) 100%);
}

.documents-content {
  margin-top: 1.6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 1.2rem;
}

.documents-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.6rem;
}

.document-item {
  font-size: 0.92rem;
  line-height: 1.4;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 0.6rem;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.document-item:hover {
  background-color: rgba(0, 0, 0, 0.03);
}

.doc-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
}

.download-icon {
  font-size: 1.1rem;
  flex-shrink: 0;
}

.doc-icon {
  font-size: 1.2rem;
  color: var(--brand-deep);
  flex-shrink: 0;
}

.doc-name {
  color: var(--muted);
  word-break: break-word;
}

.download-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  text-decoration: none;
  color: white;
  background-color: var(--brand-deep);
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 500;
  flex-shrink: 0;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.download-btn i {
  font-size: 1.1rem;
}

.download-btn:hover {
  background-color: var(--accent);
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

@media (max-width: 620px) {
  .documents-content {
    padding: 0.9rem;
  }

  .documents-list {
    grid-template-columns: 1fr;
  }

  .document-item {
    flex-direction: column;
    align-items: flex-start;
    padding: 0.6rem;
    gap: 0.6rem;
  }

  .download-btn {
    padding: 0.4rem 0.8rem;
    font-size: 0.75rem;
  }

  .download-btn i {
    font-size: 0.9rem;
  }

  .documents-list {
    gap: 0.4rem;
  }
}
</style>
