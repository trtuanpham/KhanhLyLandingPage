<script setup>
import { reactive, ref } from 'vue'

const form = reactive({
  name: '',
  email: '',
  phone: '',
  message: '',
})

const isSubmitting = ref(false)
const statusMessage = ref('')
const isError = ref(false)

const resetForm = () => {
  form.name = ''
  form.email = ''
  form.phone = ''
  form.message = ''
}

const submitForm = async () => {
  isSubmitting.value = true
  statusMessage.value = ''
  isError.value = false

  try {
    const subject = encodeURIComponent(`Liên hệ tư vấn từ ${form.name}`)
    const body = encodeURIComponent(
      [
        `Họ và tên: ${form.name}`,
        `Email: ${form.email}`,
        `Số điện thoại: ${form.phone}`,
        '',
        'Nội dung:',
        form.message,
      ].join('\n')
    )

    const mailtoLink = `mailto:ctytnhhkhanhly@gmail.com?subject=${subject}&body=${body}`
    window.location.href = mailtoLink

    statusMessage.value = 'Đã mở ứng dụng email. Vui lòng kiểm tra và bấm gửi để hoàn tất.'
    resetForm()
  } catch (error) {
    statusMessage.value = error instanceof Error ? error.message : 'Đã xảy ra lỗi không mong muốn.'
    isError.value = true
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <section id="contact" class="section contact-section">
    <div class="container contact-grid">
      <div>
        <h2 class="section-title">Liên hệ</h2>
        <p class="section-subtitle">
          Hãy chia sẻ nhu cầu dự án của bạn, đội ngũ của chúng tôi sẽ phản hồi với phương án tư vấn phù hợp.
        </p>
        <div class="contact-info">
          <div class="info-item">
            <strong>Trụ sở chính:</strong>
            <p>44/50, đường 30/4, Phường Thủ Dầu Một, TP.Hồ Chí Minh</p>
          </div>
          <div class="info-item">
            <strong>Trụ sở liên hệ:</strong>
            <p>85/17, Tổ 7, Khu phố 6, Đường 30/4, Phường Phú Lợi, Thành Phố Hồ Chí Minh</p>
          </div>
          <div class="info-item">
            <strong>Điện thoại:</strong>
            <p><a href="tel:0909593659">0909.593.659</a></p>
          </div>
          <div class="info-item">
            <strong>Email:</strong>
            <p><a href="mailto:ctytnhhkhanhly@gmail.com">ctytnhhkhanhly@gmail.com</a></p>
          </div>
        </div>
      </div>

      <form class="contact-form" @submit.prevent="submitForm">
        <label>
          Họ và tên
          <input v-model="form.name" type="text" required autocomplete="name" />
        </label>

        <label>
          Email
          <input v-model="form.email" type="email" required autocomplete="email" />
        </label>

        <label>
          Số điện thoại
          <input v-model="form.phone" type="tel" required autocomplete="tel" />
        </label>

        <label>
          Nội dung
          <textarea v-model="form.message" rows="5" required></textarea>
        </label>

        <button type="submit" :disabled="isSubmitting">
          {{ isSubmitting ? 'Đang gửi...' : 'Gửi liên hệ' }}
        </button>

        <p v-if="statusMessage" :class="['status-message', { error: isError }]">
          {{ statusMessage }}
        </p>
      </form>
    </div>
  </section>
</template>

<style scoped>
.contact-section {
  background: linear-gradient(140deg, rgba(20, 52, 73, 0.08) 0%, rgba(20, 52, 73, 0.02) 50%, rgba(234, 143, 45, 0.12) 100%);
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.7rem;
  align-items: start;
}

.contact-form {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 1.3rem;
  display: grid;
  gap: 0.9rem;
}

.contact-form label {
  font-weight: 600;
  color: var(--brand-deep);
  display: grid;
  gap: 0.35rem;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  border: 1px solid #b6c4cf;
  border-radius: 10px;
  padding: 0.7rem 0.75rem;
  font: inherit;
  color: var(--ink);
  background: #f9fbfd;
}

.contact-form input:focus,
.contact-form textarea:focus {
  outline: 2px solid rgba(31, 79, 115, 0.3);
  border-color: var(--brand);
}

.contact-form button {
  margin-top: 0.25rem;
  border: 0;
  border-radius: 10px;
  padding: 0.82rem 1rem;
  font: inherit;
  font-weight: 700;
  background: var(--brand);
  color: #eef4f8;
  cursor: pointer;
}

.contact-form button:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}

.status-message {
  margin: 0;
  color: #2f6a43;
  font-weight: 600;
}

.status-message.error {
  color: #9f2832;
}

.contact-info {
  margin-top: 1.5rem;
  display: grid;
  gap: 1rem;
}

.info-item strong {
  display: block;
  color: var(--brand-deep);
  font-weight: 600;
  margin-bottom: 0.3rem;
}

.info-item p {
  margin: 0;
  color: var(--muted);
  font-size: 0.95rem;
  line-height: 1.5;
}

.info-item a {
  color: var(--brand);
  text-decoration: none;
  transition: color 0.2s ease;
}

.info-item a:hover {
  color: var(--accent);
  text-decoration: underline;
}

@media (max-width: 860px) {
  .contact-grid {
    grid-template-columns: 1fr;
  }
}
</style>
