<template>
    <div id="app" class="chat-container">
        <msg-history :messages="messages" :username="username" />
        <msg-form v-on:formSubmit="handleNewMessage" />
    </div>
</template>

<script>
    import MessagesHistory from './components/MessagesHistory.vue'
    import Form from "./components/Form.vue"
    import axios from "axios"

    export default {
        name: 'app',
        data: () => {
            return {
                'messages' : [],
                'username': window.localStorage.getItem('authorName')
            }
        },
        mounted() {
            this.refreshList();
        },
        components: {
            'msg-history': MessagesHistory,
            'msg-form': Form
        },
        methods: {
            handleNewMessage: function(msg) {
                this.username = msg.author;
                this.messages.push(msg);

                axios({
                    method: 'post',
                    url: '/chat',
                    data: msg
                })
            },
            refreshList: function () {
                axios.get('/chat').then(response => {
                    this.messages = response.data;
                });
            }
        }
    }
</script>

<style>
    #app {
        font-size: 12px;
        font-family: Tahoma, sans-serif;
        color: #000;
    }

    .chat-container {
        margin: 0 auto;
        width: 360px;
        border: 1px solid black;
    }
</style>
