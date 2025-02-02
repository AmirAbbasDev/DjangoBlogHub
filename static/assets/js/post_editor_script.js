import { Editor } from '@tiptap/core';
import StarterKit from '@tiptap/starter-kit';

new Editor({
  element: document.getElementById('wysiwyg'),
  extensions: [StarterKit],
  content: '<p>Welcome to Flowbite!</p>',
})