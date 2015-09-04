#if !defined(__PAUSEMENU_H__)
#define __PAUSEMENU_H__

#include "scene.h"

class PauseMenu : public Scene
{
protected:
    // UI components
    CSprite*    continueGameButton;
    CSprite*    newGameButton;
public:
    CSprite*    getContinueGameButton()     { return continueGameButton; }
    CSprite*    getNewGameButton()          { return newGameButton; }

public:
    PauseMenu()  {}
    ~PauseMenu();

    // initialise the menu
    void            Init();

    // Update the menu
    void            Update(float deltaTime = 0.0f, float alphaMul = 1.0f);

    // Render the menu
    void            Render();

    // Button callbacks
    static void     continueGame(CTween* pTween);
    static void     newGame(CTween* pTween);

};

#endif  // __PAUSEMENU_H__


