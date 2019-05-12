<template>
    <div class="msg-history">
        <ul class="messages">
            <message v-for="msg in messages" :author="msg.author" :text="msg.text" :date="msg.date"
                     v-bind:key="msg.id" :username="username" />
        </ul>
    </div>
</template>

<script>
    import Message from './Message.vue'

    export default {
        name: "msg-history",
        props: ['messages', 'username'],

        components: {
            Message
        }
    }
</script>

<style scoped>
    .msg-history {
        padding: 15px;
        overflow-y: auto;
        background-color: #ECE5DD;
        flex-grow: 1;
    }

    .msg-history::-webkit-scrollbar {
        display: none;
    }

    ul.messages {
        margin: 0;
        padding: 0;
    }
</style>
