<template>
    <div id="app" class="chat-container">
        <div class="error-description" v-if="error">
            <p><strong>Error</strong></p>
            <p>{{ error }}</p>
        </div>

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
                'error': null,
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
                }).catch(err => {
                    this.error = 'Unable to save new message.';
                });
            },
            refreshList: function () {
                axios.get('/chat').then(response => {
                    this.messages = response.data;
                })
                .catch(err => {
                    this.error = 'Unable to load last messages from server.';
                })
            }
        }
    }
</script>

<style>
    body {
        margin: 0;
        padding: 0;
    }
</style>
<style>
    #app {
        font-size: 12px;
        font-family: Tahoma, sans-serif;
        color: #000;
    }

    p {
        margin-top: 0;
    }

    .chat-container {
        margin: 0 auto;
        width: 100%;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        height: 100vh;
    }

    .error-description {
        position: absolute;
        width: 100%;
        height: 50px;
        top: 0;
        padding: 15px 0;
        text-indent: 15px;
        background-color: rgba(255, 0, 0, 0.65);
        font-size: 13px;
    }
</style>
