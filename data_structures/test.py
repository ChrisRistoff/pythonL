function! SuggestOneCharacter()
    let suggestion = copilot#Accept("")
    let bar = copilot#TextQueuedForInsertion()
    return bar[0]
endfunction

function! SuggestOneWord()
    let suggestion = copilot#Accept("")
    let bar = copilot#TextQueuedForInsertion()
    return split(bar, '[ .]\zs')[0]
endfunction

imap <script><expr> <C-l> SuggestOneWord()
imap <script><expr> <C-left> SuggestOneCharacter()