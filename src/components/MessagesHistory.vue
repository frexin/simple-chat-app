<template>
    <div class="msg-history">
        <ul class="messages">
            <message v-for="msg in messages" :author="msg.author" :text="msg.text" :date="msg.date" />
        </ul>
    </div>
</template>

<script>
    import Message from './Message.vue'

    export default {
        name: "msg-history",
        props: ['messages'],

        components: {
            Message
        },
        addNewMessage(msg_data) {

        }
    }
</script>

<style scoped>
    .msg-history {
        padding: 15px;
        height: 480px;
        overflow-y: auto;
        background-color: #ECE5DD;
    }

    .msg-history::-webkit-scrollbar {
        display: none;
    }

    ul.messages {
        margin: 0;
        padding: 0;
    }
</style>
