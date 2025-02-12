<template>
  <div class="container mt-4">
    <div class="card">
      <div class="card-header bg-primary text-white">
        <h5 class="mb-0">Чат</h5>
      </div>
      <div class="card-body chat-messages">
        <div v-for="msg in messages" :key="msg.id" class="alert alert-secondary p-2">
          <strong>{{ msg.user }}:</strong> {{ msg.text }}
        </div>
      </div>
      <div class="card-footer d-flex">
        <input
          v-model="messageText"
          @keyup.enter="sendMessage"
          class="form-control me-2"
          placeholder="Введите сообщение..."
        />
        <button class="btn btn-primary" @click="sendMessage">Отправить</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from "vue";
import socket from "@/socket";

export default {
  setup() {
    const messages = ref([]);
    const messageText = ref("");
    const user = "User" + Math.floor(Math.random() * 1000);

    onMounted(() => {
      socket.on("message", (msg) => {
        messages.value.push(msg);
      });

      socket.emit("join_room", { user, room: "main" });
    });

    onUnmounted(() => {
      socket.off("message");
      socket.emit("leave_room", { user, room: "main" });
    });

    const sendMessage = () => {
      if (messageText.value.trim() !== "") {
        socket.emit("message", {
          chat_id: "main",
          user: user,
          text: messageText.value,
        });
        messageText.value = "";
      }
    };

    return { messages, messageText, sendMessage };
  },
};
</script>

<style scoped>
.chat-messages {
  max-height: 300px;
  overflow-y: auto;
}
</style>