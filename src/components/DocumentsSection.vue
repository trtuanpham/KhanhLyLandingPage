<script setup>
const handleView = (filePath) => {
  window.open(filePath, '_blank');
};

const documentSections = [
  {
    category: "Giấy chứng nhận & Đăng ký kinh doanh",
    documents: [
      { name: "Chứng nhận đào tạo", file: "/scans/CHUNG_NHAN_DAO_TAO.pdf" },
      { name: "Giấy chứng nhân hoàn thành", file: "/scans/GIAY_CHUNG_NHAN_HOAN_THANH.pdf" },
      { name: "Giấy đăng ký kinh doanh", file: "/scans/GIAY_DANG_KY_KINH_DOANH.pdf" },
    ],
  },
  {
    category: "Hồ sơ năng lực phòng LAB",
    documents: [
      { name: "Mẫu số 01 - Công bố thông tin về năng lực đủ điều kiện hoạt động thí nghiệm", file: "/scans/MAU_SO_01_TT_NANG_LUC_DU_DK_HDONG_THI_NGHIEM.pdf", allowDownload: false },
      { name: "Mẫu số 02 - Công bố thông tin dừng hoạt động thí nghiệm", file: "/scans/MAU_SO_02_CONG_BO_TT_DUNG_HOAT_DONG_THI_NGHIEM.pdf", allowDownload: false },
      {
        name: "1. Đơn công bố năng lực hoạt động phòng thí nghiệm Khánh Lý",
        file: "/scans/Documents/1.DON_CONG_BO_NANG_LUC_HOAT_DONG_PHONG_THI_NGHIEM_KHANH_LY.pdf",
        allowDownload: false,
      },
      {
        name: "2. Danh sách cán bộ quản lý, thí nghiệm viên kèm theo các văn bằng",
        file: "/scans/Documents/2._DANH_SACH_CAN_BO_QUAN_LY_THI_NGHIEM_VIEN_KEM_THEO_CAC_VAN_BANG.pdf",
        allowDownload: false,
      },
      {
        name: "3. Giấy chứng nhận đăng ký kinh doanh nghiệp và GCN địa điểm kinh doanh",
        file: "/scans/Documents/3.GIAY_CHUNG_NHAN_DANG_KY_KINH_DOANH__NGHIEP_VA_GCN_DANG_KY_DIA_DIEM_KINH_DOANH.pdf",
        allowDownload: false,
      },
      { name: "4. Quyết định thành lập phòng thí nghiệm chuyên ngành xây dựng", file: "/scans/Documents/4.QUYET_DINH_THANH_LAP_PHONG_THI_NGHIEM_CHUYEN_NGANH_XAY_DUNG_.pdf", allowDownload: false },
      { name: "5. Quyết định bổ nhiệm trưởng phòng - phó phòng", file: "/scans/Documents/5.QUYET_DINH_BO_NHIEM_TRUONG_PHONG_-_PHO_PHONG.pdf", allowDownload: false },
      { name: "6. Danh sách cán bộ, thí nghiệm viên và bản phân công công việc", file: "/scans/Documents/6.DANH_SACH_CAN_BO_THI_NGHIEM_VIEN_VA_BAN_PHAN_CONG_CONG_VIEC_.pdf", allowDownload: false },
      {
        name: "7. Danh mục các tài liệu, quy trình quản lý chất lượng - tiêu chuẩn kỹ thuật",
        file: "/scans/Documents/7.DANH_MUC_CAC_TAI_LIEU_QUY_TRINH_QUAN_LY_CHAT_LUONG-_TCKY_THUAT_.pdf",
        allowDownload: false,
      },
      {
        name: "8. Danh mục dụng cụ - thiết bị - hợp đồng mua bán - hóa đơn thiết bị Khánh Lý",
        file: "/scans/Documents/8._DANH_MUC_DUNG_CU_-_THIET_BI_-_HOP_DONG_MUA_BAN_HOA_DON_THIET_BI_KHANH_LY.pdf",
        allowDownload: false,
      },
      { name: "9. Chứng chỉ kiểm định, hiệu chuẩn các thiết bị thí nghiệm", file: "/scans/Documents/9.CHUNG_CHI_KIEM_DINH_HIEU_CHUAN_CAC_THIET_BI_THI_NGHIEM_.pdf", allowDownload: false },
      { name: "10. Hợp đồng lao động nhân viên", file: "/scans/Documents/10._HOP_DONG_LAO_DONG_NHAN_VIEN.pdf", allowDownload: false },
      {
        name: "11. Hợp đồng thuê nhà hoặc giấy tờ chứng minh quyền sử dụng đất và bản vẽ mặt bằng",
        file: "/scans/Documents/11.HOP_DONG_THUE_NHA_HOAC_GIAY_TO_CHUNG_MINH_QUYEN_SU_DUNG__DAT_VA_BAN_VE_MAT_BANG_BO_TRI_THIET_BI_PTN.pdf",
        allowDownload: false,
      },
      { name: "12. Sổ tay chất lượng, các quy trình, thủ tục ISO 17025", file: "/scans/Documents/12._SO_TAY_CHAT_LUONG_CAC_QUY_TRINH_THU_TUC_ISO_17025_.pdf", allowDownload: false },
      { name: "13. Tiêu chuẩn kỹ thuật nước ngoài", file: "/scans/Documents/13.TIEU_CHUAN_KY_THUAT_NUOC_NGOAI_(NEU_CO).pdf", allowDownload: false },
    ],
  },
];

const handleDownload = (event, docName) => {
  if (!confirm(`Bạn có muốn tải file "${docName}" không?`)) {
    event.preventDefault();
  }
};
</script>

<template>
  <section id="documents" class="section documents">
    <div class="container">
      <h2 class="section-title">Tài liệu</h2>
      <p class="section-subtitle">Giấy chứng nhận, giấy phép kinh doanh và các tài liệu liên quan đến năng lực hoạt động của công ty</p>

      <div class="documents-sections">
        <div v-for="section in documentSections" :key="section.category" class="documents-content" :id="section.category === 'Hồ sơ năng lực phòng LAB' ? 'lab-qualifications' : undefined">
          <h3 class="section-category">{{ section.category }}</h3>
          <ul class="documents-list">
            <li v-for="(doc, index) in section.documents" :key="index" class="document-item">
              <div class="doc-info">
                <i class="material-icons doc-icon">description</i>
                <span class="doc-name">{{ doc.name }}</span>
              </div>
              <template v-if="!doc.allowDownload">
                <button :title="`Xem ${doc.name}`" class="action-btn view-btn" @click="handleView(doc.file)">
                  <i class="material-icons">visibility</i>
                  Xem
                </button>
              </template>
              <template v-else>
                <a :href="doc.file" :title="`Tải ${doc.name}`" class="action-btn download-btn" @click="handleDownload($event, doc.name)">
                  <i class="material-icons">download</i>
                  Tải xuống
                </a>
              </template>
            </li>
          </ul>
        </div>
      </div>


    </div>
  </section>
</template>

<style scoped>
.documents {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.74) 0%, rgba(226, 235, 241, 0.86) 100%);
}

.documents-sections {
  margin-top: 1.6rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.documents-content {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 1.2rem;
}

.section-category {
  margin: 0 0 1rem 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--brand-deep);
  border-bottom: 2px solid var(--brand-deep);
  padding-bottom: 0.5rem;
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

.action-btn {
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
  border: none;
  cursor: pointer;
}

.action-btn i {
  font-size: 1.1rem;
}

.action-btn:hover {
  background-color: var(--accent);
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.download-btn {
  /* inherits from .action-btn */
}

.view-btn {
  background-color: #17a2b8;
}

.view-btn:hover {
  background-color: #138496;
}

@media (max-width: 620px) {
  .documents-sections {
    gap: 0.9rem;
  }

  .documents-content {
    padding: 0.9rem;
  }

  .section-category {
    font-size: 0.95rem;
    margin-bottom: 0.8rem;
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

  .action-btn {
    padding: 0.4rem 0.8rem;
    font-size: 0.75rem;
  }

  .action-btn i {
    font-size: 0.9rem;
  }

  .documents-list {
    gap: 0.4rem;
  }
}

/* PDF Modal Styles */
.pdf-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 999;
}

.pdf-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.pdf-modal-content {
  background: white;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  max-width: 900px;
  width: 100%;
  height: 90vh;
  max-height: 800px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.pdf-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  border-bottom: 1px solid #e0e0e0;
  background-color: var(--surface);
  border-radius: 8px 8px 0 0;
}

.pdf-modal-header h3 {
  margin: 0;
  font-size: 1rem;
  color: var(--brand-deep);
  flex: 1;
  word-break: break-word;
  padding-right: 1rem;
}

.close-btn {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  color: #666;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.close-btn:hover {
  background-color: rgba(0, 0, 0, 0.05);
  color: #000;
}

.pdf-modal-body {
  flex: 1;
  overflow: auto;
  padding: 0;
}

.pdf-modal-body iframe {
  width: 100%;
  height: 100%;
  border: none;
}

@media (max-width: 768px) {
  .pdf-modal {
    padding: 0.5rem;
  }

  .pdf-modal-content {
    max-height: calc(100vh - 1rem);
    border-radius: 8px;
  }

  .pdf-modal-header {
    padding: 0.75rem;
  }

  .pdf-modal-header h3 {
    font-size: 0.9rem;
    padding-right: 0.5rem;
  }

  .close-btn {
    width: 32px;
    height: 32px;
  }
}
</style>
