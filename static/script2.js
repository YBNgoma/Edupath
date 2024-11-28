(function () {
    var Message;
    Message = function (arg) {
      this.text = arg.text, this.message_side = arg.message_side;
      this.draw = function (_this) {
        return function () {
          var $message;
          $message = $($('.message_template').clone().html());
          $message.addClass(_this.message_side).find('.text').html(_this.text);
          $('.messages').append($message);
          return setTimeout(function () {
            return $message.addClass('appeared');
          }, 0);
        };
      }(this);
      return this;
    };
    $(function () {
      var getMessageText, message_side, sendMessage;
      message_side = 'right';
      getMessageText = function () {
          var $message_input;
          $message_input = $('.message_input');
          return $message_input.val();
      };


      sendMessage = function (text) {
      var $messages, message;
      if (text.trim() === '') {
          return;
      }
      $('.message_input').val('');
      $messages = $('.messages');

      // Set message_side based on whether the message is from the user or chatbot
      var message_side = 'right';

      message = new Message({
        text: text,
        message_side: message_side
      });

      // Draw user message
      message.draw();

      // Call getResponse() to get the chatbot's response
      $.get("/get", { msg: text }).done(function(data) {
        var botMessage = new Message({
            text: data,
            message_side: 'left'
        });
        // Draw bot message
        botMessage.draw();
        $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
      });

      return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
      };

      $('.send_message').click(function (e) {
        return sendMessage(getMessageText());
      });
      $('.message_input').keyup(function (e) {
        if (e.which === 13) {
          return sendMessage(getMessageText());
        }
      });
      // Add "Writing..." message
      writingMessage = new Message({
        text: 'Your AI-powered career guidance chatbot here , Just send a prompt!',
        message_side: 'left'
      });
      writingMessage.draw();
    });
  }.call(this));

  function openContainer(evt, containerName) {
    var i, containers, icons;
  
    // Get all container elements
    containers = document.getElementsByClassName("menu-icon-container");
  
    // Hide all containers
    for (i = 0; i < containers.length; i++) {
      containers[i].style.display = "none";
    }
  
    // Get all icon elements
    icons = document.getElementsByClassName("icon-bar")[0].getElementsByTagName("a");
  
    // Remove "active" class from all icons
    for (i = 0; i < icons.length; i++) {
      icons[i].className = icons[i].className.replace(" active", "");
    }
  
    // Show the selected container
    document.getElementById(containerName).style.display = "block";
  
    // Add "active" class to the selected icon
    evt.currentTarget.className += " active";
  }

  function logout() {
    // Implement logout functionality here
    alert('Logout clicked');
    window.location.href = 'authenticate.html';
  }

  const inputField = document.getElementById('nameinput');
        const labelText = document.getElementById('namelabel');
        const editButton = document.getElementById('editButton');
        
        editButton.addEventListener('click', function() {
          namelabel.textContent = nameinput.value;
          inputField.value = ''; // Clear the input field after updating the label
        });

  function getData() {
            // Get the input element
            var input = document.getElementById("myInput");
      
            // Get the value from the input element
            var inputValue = input.value;
      
            // Set the value of the label to the input value
            var label = document.getElementById("myLabel");
            label.innerText = inputValue;
          }
          
          var container = document.getElementById('chat-window-container');
          var shadow = container.attachShadow({ mode: 'open' });

          var style = document.createElement('style');
          style.textContent = 
            
            shadow.appendChild(style);